import sys
import os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']  # 解决 Pyinstaller 报错

import mainwindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
import myserialthread
import re
import myhttp
import mylogger


class MyMainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 日志
        self._mylogger = mylogger.MyLogger(out=1).getLogger()

        # 设置输入范围
        my_regex = QtCore.QRegExp("^(([3-4][0-9])(\\.\\d{1,2})?)$")  # 30.00 - 49.99
        my_validator = QtGui.QRegExpValidator(my_regex, self.ui_lne_temperature)
        self.ui_lne_temperature.setValidator(my_validator)
        self.ui_lne_temperature_max.setValidator(my_validator)
        self.ui_lne_temperature_min.setValidator(my_validator)

        # 信号槽
        self.ui_btn_refresh.clicked.connect(self.refreshEvent)
        self.ui_btn_connect.clicked.connect(self.openEvent)
        self.ui_btn_OK.clicked.connect(self.okEvent)
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.updateAlarmEvent)

        self._serial_thread = myserialthread.SerialThread()  # 串口线程
        self._serial_thread._id_signal.connect(self.receiveQrCodeEvent)  # 接收ID信号
        self._serial_thread._status_signal.connect(self.updateConnectStatusEvent)  # 接收连接状态信号
        self._is_open = False  # 连接状态
        self._is_ok = False  # 报警
        self._flag = 0  # 0员工 1访客
        self._visitor_info = dict()  # 当前扫码的人员信息

        # self.ui_btn_refresh.click()  # 刷新，扫描端口
        self.autoConnect()

        self._mylogger.debug('debug级别，一般用来打印一些调试信息，级别最低')
        self._mylogger.info('info级别，一般用来打印一些正常的操作信息')
        self._mylogger.warning('waring级别，一般用来打印警告信息')
        self._mylogger.error('error级别，一般用来打印一些错误信息')
        self._mylogger.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')

    # 打开界面，自动连接
    def autoConnect(self):
        port_list = self._serial_thread.scanPort()
        if port_list is None:
            return
        com = ''
        for port in port_list:
            if port:
                self.ui_cb_com.addItem(port[0])
                if port[1] and 'USB 串行设备' in port[1]:
                    com = port[0]
        if com == '':
            return
        try:
            if self._serial_thread.openPort(com):  # 打开串口
                # 线程启动
                self._serial_thread.start()
                # 界面更新
                self.ui_btn_connect.setText('关闭')
                self.ui_btn_refresh.setDisabled(True)
                self.ui_cb_com.setDisabled(True)
                self._timer.start(300)
        except Exception as ex:
            print(ex)
            return

    # 体温是否正常
    def temperature_is_ok(self):
        try:
            temp = self.ui_lne_temperature.text()
            temp = float(0 if temp == '' else temp)
            temp_max = float(self.ui_lne_temperature_max.text())
            temp_min = float(self.ui_lne_temperature_min.text())
        except Exception as ex:
            print(ex)
            return
        return True if (temp >= temp_min) and (temp <= temp_max) else False

    # 刷新报警
    def updateAlarmEvent(self):
        is_ok = self.temperature_is_ok()
        # print(is_ok)
        if is_ok != self._is_ok:
            if is_ok:
                self.ui_lab_alarm.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                self.ui_lab_alarm.setStyleSheet("background-color: rgb(255, 0, 0);")
        self._is_ok = is_ok

    # 刷新按键
    def refreshEvent(self):
        port_list = self._serial_thread.scanPort()
        self.ui_cb_com.clear()
        if port_list is None:
            return
        for port in port_list:
            if port:
                self.ui_cb_com.addItem(port[0])

    # 打开按键
    def openEvent(self):
        port = self.ui_cb_com.currentText()
        if port == '':
            QMessageBox.information(self, "提示", '没有可用串口')
            return
        if self.ui_btn_connect.text() == '打开':  # 打开
            try:
                if self._serial_thread.openPort(port):  # 打开串口
                    # 线程启动
                    self._serial_thread.start()
                    # 界面更新
                    self.ui_btn_connect.setText('关闭')
                    self.ui_btn_refresh.setDisabled(True)
                    self.ui_cb_com.setDisabled(True)
                    self._timer.start(300)
            except Exception as ex:
                print(ex)
                return
        else:  # 关闭
            try:
                # 线程暂停
                self._serial_thread.terminate()  # 线程中止
                self._serial_thread.wait()  # 中止的线程并不能立即停止，等待期完全中止
                # 关闭串口
                self._serial_thread.closePort()
                # 界面更新
                self.ui_btn_connect.setText('打开')
                self.ui_btn_refresh.setDisabled(False)
                self.ui_cb_com.setDisabled(False)
                self._timer.stop()
            except Exception as ex:
                print(ex)
                return

        self.updateConnectStatusEvent(self._serial_thread.portIsOpen())

    # 更新连接状态
    def updateConnectStatusEvent(self, is_open):
        if is_open != self._is_open:
            if is_open:
                self.ui_lab_status.setStyleSheet("border-image: url(:/img/io_green.png);")
            else:
                self.ui_lab_status.setStyleSheet("border-image: url(:/img/io_red.png);")
        self._is_open = is_open

    # 接收二维码，并处理
    def receiveQrCodeEvent(self, url):
        # https://www.baidu.com?flag=0&visitCode=216555
        # url = 'https://www.baidu.com?flag=1&visitCode=17750526667'
        #        47.96.172.122:8066/view/InfoExhibition.html?flag=0&visitCode=273
        # flag（0员工，1访客）
        # visitCode（员工：身份证后六位，访客：手机号）
        try:
            flag = re.compile(r'(?<=flag=)[0-1]').search(url).group()  # r'(?<=visitCode=)\d+\.?\d*'
            print(flag)
            visit_code = re.compile(r'(?<=visitCode=)\d{6,}').search(url).group()
            print(visit_code)
        except Exception as ex:
            print(ex)
            QMessageBox.information(self, "提示", "无效二维码！")
            return

        # 获取人员信息
        self.ui_lw_visitor_info.clear()  # 清除信息
        if flag == '0':  # 员工
            self._visitor_info = myhttp.QueryUserByCode(visit_code)
        elif flag == '1':  # 访客
            self._visitor_info = myhttp.QueryVisitorByCode(visit_code)
        if len(self._visitor_info) == 0:
            QMessageBox.information(self, "提示", "查询失败！")
            return  # 错误

        # 字段转中文
        my_shift = {
            "UserId": "员工ID",
            "Name": "姓名",
            "Phone": "手机",
            "Sex": "性别",
            "Company": "公司",
            "Department": "部门",
            "VisitCode": "身份证后6位",
            "Job": "职位",

            "ID": "访客ID",
            # "Name": "姓名",
            # "Phone": "手机",
            "Domicile": "户籍",
            "FromPlace": "来源地",
            "VisitTo": "拜访人",
            "VisitOrigin": "来访事由",
            "TripRecd": "14天出行信息",
            "EntryTime": "进入时间",
            "Healthy": "健康",
            "Temperature": "体温"
        }

        for key, value in self._visitor_info.items():
            self.ui_lw_visitor_info.addItem(f'{my_shift[key] if key in my_shift.keys() else key}: {value}')  # 打印信息

    # 提交按键
    def okEvent(self):
        res = QMessageBox.information(self, "提示", "确定提交？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        msg = ''

        if len(self._visitor_info) == 0:
            QMessageBox.information(self, "提示", "请先扫描二维码！")
            return

        healthy = '是' if self.temperature_is_ok() else '否'
        temperature = self.ui_lne_temperature.text()

        if res == QMessageBox.Yes:
            if self._flag == 0:
                user_id = self._visitor_info['UserId']
                msg = myhttp.StaffEntry(user_id, healthy, temperature)['msg']
            elif self._flag == 1:
                id = self._visitor_info['ID']
                msg = myhttp.VisitEntry(id, healthy, temperature)['msg']
        QMessageBox.information(self, "提示", msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

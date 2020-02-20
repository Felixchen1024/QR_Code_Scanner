import sys
import time
import serial
import serial.tools.list_ports
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal


class SerialThread(QtCore.QThread):
    # 信号
    _id_signal = pyqtSignal(str)
    _status_signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(SerialThread, self).__init__(parent)
        # 初始化串口
        self._serial = serial.Serial()
        self._serial.port = None  # self.scan()[0][0]  # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
        self._serial.baudrate = 9600  # 波特率，9600,19200,38400,57600,115200
        self._serial.timeout = 1  # 超时设置，None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        self._stop = False

    def scanPort(self):
        port_list = list(serial.tools.list_ports.comports())
        port_list.sort()
        print(port_list)
        if len(port_list) == 0:
            print('没有可用串口')
        else:
            for p in port_list:
                print(p)
            return port_list

    def openPort(self, port=0):
        self._serial.port = port
        self._serial.open()

        if self._serial.isOpen():
            print('串口打开成功')
            return True
        else:
            print('串口打开失败')
            return False

    def closePort(self):
        if self._serial.isOpen():
            self._serial.close()
            print('串口关闭')

    def portIsOpen(self):
        return self._serial.isOpen()

    def run(self):
        # self._status_signal.emit(self._serial.isOpen())  # 发送状态信号
        while not self._stop:
            try:
                # n = self._serial.inWaiting()
                # id = ''
                if self._serial.inWaiting():
                    # print(read())#读一个字节
                    # print(read(10).decode("gbk"))#读十个字节
                    # print(readline().decode("gbk"))#读一行
                    # print(readlines())#读取多行，返回列表，必须匹配超时（timeout)使用
                    # print(in_waiting)#获取输入缓冲区的剩余字节数
                    # print(out_waiting)#获取输出缓冲区的字节数

                    # url = self._serial.read(n).decode('utf-8')
                    url = self._serial.readline().decode('utf-8')
                    print('recv' + ' ' + time.strftime("%Y-%m-%d %X") + ' ' + url.strip())
                    self._id_signal.emit(url.strip())  # 发送二维码URL信号
            except Exception as ex:
                print(ex)

    def stop(self):
        self._stop = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ThreadComID = SerialThread()
    ThreadComID.open('com3')
    ThreadComID.start()
    sys.exit(app.exec_())

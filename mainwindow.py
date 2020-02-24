# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox\n"
"{\n"
"    border: 3px solid;\n"
"    border-top-color: rgb(167, 201, 247);\n"
"    border-left-color: none;\n"
"    border-right-color: none;\n"
"    border-bottom-color: none;\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ui_btn_connect = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_btn_connect.sizePolicy().hasHeightForWidth())
        self.ui_btn_connect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ui_btn_connect.setFont(font)
        self.ui_btn_connect.setStyleSheet("QPushButton {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background: rgb(120, 174, 249);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background: rgb(223, 220, 220);\n"
"}")
        self.ui_btn_connect.setObjectName("ui_btn_connect")
        self.gridLayout_4.addWidget(self.ui_btn_connect, 0, 2, 1, 1)
        self.ui_cb_com = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_cb_com.sizePolicy().hasHeightForWidth())
        self.ui_cb_com.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ui_cb_com.setFont(font)
        self.ui_cb_com.setObjectName("ui_cb_com")
        self.gridLayout_4.addWidget(self.ui_cb_com, 0, 0, 1, 1)
        self.ui_btn_refresh = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_btn_refresh.sizePolicy().hasHeightForWidth())
        self.ui_btn_refresh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ui_btn_refresh.setFont(font)
        self.ui_btn_refresh.setStyleSheet("QPushButton {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background: rgb(120, 174, 249);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background: rgb(223, 220, 220);\n"
"}")
        self.ui_btn_refresh.setObjectName("ui_btn_refresh")
        self.gridLayout_4.addWidget(self.ui_btn_refresh, 0, 1, 1, 1)
        self.ui_lab_status = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_lab_status.sizePolicy().hasHeightForWidth())
        self.ui_lab_status.setSizePolicy(sizePolicy)
        self.ui_lab_status.setMinimumSize(QtCore.QSize(50, 50))
        self.ui_lab_status.setStyleSheet("#ui_lab_status{\n"
"border-image: url(:/img/is_open_off.png);\n"
"}")
        self.ui_lab_status.setText("")
        self.ui_lab_status.setObjectName("ui_lab_status")
        self.gridLayout_4.addWidget(self.ui_lab_status, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("QGroupBox\n"
"{\n"
"    border: 3px solid;\n"
"    border-top-color: rgb(167, 201, 247);\n"
"    border-left-color: none;\n"
"    border-right-color: none;\n"
"    border-bottom-color: none;\n"
"}")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ui_lw_visitor_info = QtWidgets.QListWidget(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ui_lw_visitor_info.setFont(font)
        self.ui_lw_visitor_info.setStyleSheet("")
        self.ui_lw_visitor_info.setObjectName("ui_lw_visitor_info")
        self.gridLayout_5.addWidget(self.ui_lw_visitor_info, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox\n"
"{\n"
"    border: 3px solid;\n"
"    border-top-color: rgb(167, 201, 247);\n"
"    border-left-color: none;\n"
"    border-right-color: none;\n"
"    border-bottom-color: none;\n"
"}\n"
"QLineEdit{\n"
"    border: 3px solid rgb(180, 208, 246);\n"
"}")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(9, 9, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.ui_lne_temperature_min = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_lne_temperature_min.sizePolicy().hasHeightForWidth())
        self.ui_lne_temperature_min.setSizePolicy(sizePolicy)
        self.ui_lne_temperature_min.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.ui_lne_temperature_min.setFont(font)
        self.ui_lne_temperature_min.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui_lne_temperature_min.setStyleSheet("")
        self.ui_lne_temperature_min.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_lne_temperature_min.setReadOnly(True)
        self.ui_lne_temperature_min.setObjectName("ui_lne_temperature_min")
        self.gridLayout.addWidget(self.ui_lne_temperature_min, 1, 1, 1, 1)
        self.ui_lne_temperature_max = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_lne_temperature_max.sizePolicy().hasHeightForWidth())
        self.ui_lne_temperature_max.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.ui_lne_temperature_max.setFont(font)
        self.ui_lne_temperature_max.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui_lne_temperature_max.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_lne_temperature_max.setReadOnly(True)
        self.ui_lne_temperature_max.setObjectName("ui_lne_temperature_max")
        self.gridLayout.addWidget(self.ui_lne_temperature_max, 1, 2, 1, 1)
        self.ui_lne_temperature = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.ui_lne_temperature.setFont(font)
        self.ui_lne_temperature.setStyleSheet("")
        self.ui_lne_temperature.setText("")
        self.ui_lne_temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_lne_temperature.setObjectName("ui_lne_temperature")
        self.gridLayout.addWidget(self.ui_lne_temperature, 3, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.ui_lab_alarm = QtWidgets.QLabel(self.groupBox)
        self.ui_lab_alarm.setStyleSheet("#ui_lab_alarm{\n"
"border-image: url(:/img/health_abnormal.png);\n"
"}")
        self.ui_lab_alarm.setText("")
        self.ui_lab_alarm.setObjectName("ui_lab_alarm")
        self.gridLayout.addWidget(self.ui_lab_alarm, 4, 0, 1, 4)
        self.ui_btn_OK = QtWidgets.QPushButton(self.groupBox)
        self.ui_btn_OK.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.ui_btn_OK.setFont(font)
        self.ui_btn_OK.setStyleSheet("QPushButton {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background: rgb(120, 174, 249);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background: rgb(223, 220, 220);\n"
"}")
        self.ui_btn_OK.setObjectName("ui_btn_OK")
        self.gridLayout.addWidget(self.ui_btn_OK, 5, 0, 1, 4)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "体温登记"))
        self.groupBox_3.setTitle(_translate("MainWindow", "连接扫描枪"))
        self.ui_btn_connect.setText(_translate("MainWindow", "打开"))
        self.ui_btn_refresh.setText(_translate("MainWindow", "刷新"))
        self.groupBox_4.setTitle(_translate("MainWindow", "人员信息"))
        self.groupBox.setTitle(_translate("MainWindow", "健康状况"))
        self.ui_lne_temperature_min.setText(_translate("MainWindow", "36.0"))
        self.ui_lne_temperature_max.setText(_translate("MainWindow", "37.2"))
        self.label_2.setText(_translate("MainWindow", "正常范围"))
        self.label.setText(_translate("MainWindow", "当前体温"))
        self.ui_btn_OK.setText(_translate("MainWindow", "放行"))
        self.ui_btn_OK.setShortcut(_translate("MainWindow", "Return"))
import res

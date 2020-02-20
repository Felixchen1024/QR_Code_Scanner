import threading
import time
import serial
import serial.tools.list_ports
from PyQt5 import QtCore


class SerialPort:
    def __init__(self):
        # 初始化串口
        self.my_serial = serial.Serial()
        self.my_serial.port = None  # self.scan()[0][0]  # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
        self.my_serial.baudrate = 9600  # 波特率，9600,19200,38400,57600,115200
        self.my_serial.timeout = 1  # 超时设置，None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        self.alive = False
        self.waitEnd = None
        self.thread_read = None
        # self.thread_send = None

    def scan(self):
        port_list = list(serial.tools.list_ports.comports())
        print(port_list)
        if len(port_list) == 0:
            print('无可用串口')
        else:
            for p in port_list:
                print(p)
            return port_list

    def waiting(self):
        # 等待event停止标志
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def open(self, port = 0):
        self.my_serial.port = port
        self.my_serial.open()

        if self.my_serial.isOpen():
            self.waitEnd = threading.Event()
            self.alive = True

            self.thread_read = threading.Thread(target=self.reader)
            self.thread_read.setDaemon(True)

            # self.thread_send = threading.Thread(target=self.sender)
            # self.thread_send.setDaemon(True)

            self.thread_read.start()
            # self.thread_send.start()

            print('串口打开成功')
            return True
        else:
            print('串口打开失败')
            return False

    def reader(self):
        while self.alive:
            try:
                n = self.my_serial.inWaiting()
                data = ''
                if n:
                    # print(read())#读一个字节
                    # print(read(10).decode("gbk"))#读十个字节
                    # print(readline().decode("gbk"))#读一行
                    # print(readlines())#读取多行，返回列表，必须匹配超时（timeout)使用
                    # print(in_waiting)#获取输入缓冲区的剩余字节数
                    # print(out_waiting)#获取输出缓冲区的字节数

                    data = self.my_serial.read(n).decode('utf-8')
                    print('recv' + ' ' + time.strftime("%Y-%m-%d %X") + ' ' + data.strip())
                    # if len(data) == 1 and ord(data[len(data) - 1]) == 113:  # 收到字母q，程序退出
                    #     break
            except Exception as ex:
                print(ex)

        self.waitEnd.set()
        self.alive = False

    def sender(self):
        while self.alive:
            try:
                snddata = input("input data:\n")
                self.my_serial.write(snddata.encode('utf-8'))
                print('sent' + ' ' + time.strftime("%Y-%m-%d %X"))
            except Exception as ex:
                print(ex)

        self.waitEnd.set()
        self.alive = False

    def stop(self):
        self.alive = False
        # self.thread_read.join()
        # self.thread_send.join()
        if self.my_serial.isOpen():
            self.my_serial.close()


if __name__ == '__main__':
    ser = SerialPort()
    port = ser.scan()[0][0]  # 界面输入

    try:
        if ser.open(port):
            ser.waiting()
            ser.stop()
        else:
            pass
    except Exception as ex:
        print(ex)

    if ser.alive:
        ser.stop()

    del ser

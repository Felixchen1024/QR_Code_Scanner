# 文字转语音：http://tools.bugscaner.com/tts/

# from pygame import mixer
# import time
#
# mixer.init()
# mixer.music.load(r'./mp3/staff.mp3')
# mixer.music.play()
# time.sleep(1)
# mixer.music.stop()

from playsound import playsound


def PlayMp3Staff():  # 内部员工
    playsound(r'./mp3/Staff.mp3')


def PlayMp3Visitor():  # 拜访人员
    playsound(r'./mp3/Visitor.mp3')


def PlayMp3ValidationFailed():  # 验证失败
    playsound(r'./mp3/ValidationFailed.mp3')


def PlayMp3QueryFailed():  # 查询失败
    playsound(r'./mp3/QueryFailed.mp3')


if __name__ == '__main__':
    PlayMp3Staff()
    PlayMp3Visitor()
    PlayMp3ValidationFailed()
    PlayMp3QueryFailed()

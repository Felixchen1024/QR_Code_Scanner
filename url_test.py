# https://www.baidu.com?flag=0&visitCode=216555
# url = 'https://www.baidu.com?flag=1&visitCode=17750526667'
#        47.96.172.122:8066/view/InfoExhibition.html?flag=0&visitCode=273
# flag（0员工，1访客）
# visitCode（员工：身份证后六位，访客：手机号）

import re


url = 'https://www.baidu.com?flag=0&visitCode=2AC55X'
try:
    flag = re.compile(r'(?<=flag=)[0-1]').search(url).group()  # r'(?<=visitCode=)\d+\.?\d*'
    flag = int(flag)
    visit_code = re.compile(r'(?<=visitCode=)[0-9a-zA-z]{6,}').search(url).group()
    print(flag, visit_code)
except Exception as ex:
    print(ex)
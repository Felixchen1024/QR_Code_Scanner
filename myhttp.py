import requests
import json


def QueryUserByCode(visit_code):  # 按身份证后6位获取员工信息
    try:
        postdata = {'VisitCode': visit_code}  # 身份证后6位
        res = requests.post("http://119.3.66.94:6002/VisitCtl/User/QueryUserByCode", data=postdata)
        user_info = json.loads(res.json())
        if len(user_info) == 0:
            return dict()
        user_info = user_info[0]
        print(type(user_info), user_info)
        return user_info
    except Exception as ex:
        print(ex)
        return dict()

def StaffEntry(UserId, Healthy, Temperature):  # 员工进入确认
    try:
        postdata = {'UserId': UserId, 'Healthy': Healthy, 'Temperature': Temperature}
        res = requests.post("http://119.3.66.94:6002/VisitCtl/User/StaffEntry", data=postdata)
        ack = res.json()
        print(type(ack), ack)
        return ack
    except Exception as ex:
        print(ex)
        return dict()


def StaffTemperatureUpdate(UserId, Temperature):
    try:
        postdata = {'UserId': UserId, 'Temperature': Temperature}
        res = requests.post("http://119.3.66.94:6002/VisitCtl/User/StaffTemperatureUpdate", data=postdata)
        ack = res.json()
        print(type(ack), ack)
        return ack
    except Exception as ex:
        print(ex)
        return dict()


def QueryVisitorByCode(visit_code):  # 按手机号获取访客信息
    try:
        postdata = {'VisitCode': visit_code}  # 手机
        res = requests.post("http://119.3.66.94:6002/VisitCtl/User/QueryVisitorByCode", data=postdata)
        visitor_info = json.loads(res.json())
        if len(visitor_info) == 0:
            return dict()
        visitor_info = visitor_info[0]
        print(type(visitor_info), visitor_info)
        return visitor_info
    except Exception as ex:
        print(ex)
        return dict()


def VisitEntry(ID, Healthy, Temperature):  # 拜访进入确认(保安测完体温，检查信息后确认)
    try:
        postdata = {'ID': ID, 'Healthy': Healthy, 'Temperature': Temperature}
        res = requests.post("http://119.3.66.94:6002/VisitCtl/User/VisitEntry", data=postdata)
        ack = res.json()
        print(type(ack), ack)
        return ack
    except Exception as ex:
        print(ex)
        return dict()


def VisitTemperatureUpdate(ID, Temperature):
    try:
        postdata = {'ID': ID, 'Temperature': Temperature}
        res = requests.post("http://119.3.66.94:6002/VisitCtl/User/VisitTemperatureUpdate", data=postdata)
        ack = res.json()
        print(type(ack), ack)
        return ack
    except Exception as ex:
        print(ex)
        return dict()


if __name__ == '__main__':
    # res = QueryUserByCode('216555')  # 216555
    # print(res['UserId'])
    #
    # for key, value in res.items():
    #     print(key, value)

    # res = StaffEntry('71', '是', '')
    # print(res)

    # res = StaffTemperatureUpdate(71, '37.2')
    # print(res)

    # res = QueryVisitorByCode('18559517777')  # 19959793115 18559517777
    # print(res)
    # for key, value in res.items():
    #     print(key, value)

    # VisitEntry('100001', '是', '37.0')

    res = VisitTemperatureUpdate(100024, '-')
    print(res)




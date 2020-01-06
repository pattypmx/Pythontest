# 模拟车站进站
# -安检：
#   没有危险品，可以进站
#       有车票，可以上车
#       没有车票，不可以上车
#   有危险品，不可以进站

# 定义一个变量dangerous_goods,true为没有
dangerous_goods = True
ticket = 1#1为有票
if dangerous_goods:
    print("没有危险品，可以进站")
    if ticket == 1:
        print("有车票，可以上车")
    else:
        print("有车票，可以上车")
else:
    print("有危险品，不可以进站")
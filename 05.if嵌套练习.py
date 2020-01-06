# 上公交车，并且有座位可以坐下
# 刷公交卡，余额超过2元，可以上公交车；有空座位，就可以坐下

balance = int(input("余额为："))
seat = not True #true为有座位
if balance >= 2:
    print("可以上公交")
    if seat:
        print("可以坐下")
    else:
        print("没有座位，只能站着啦")
else:
    print("余额不足，不可以上车")
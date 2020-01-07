# 导入随机数
import random

# 如果需要一直执行，就使用 while true
while True:
    player = int(input("请输入：剪刀（0），石头（1），布（2）:"))
    # 定义电脑输入的随机数
    computer = random.randint(0, 2)    # random随机数，randint（0, 2）=[0, 2]

    print("玩家:%d" % player)
    print("电脑:%d" % computer)

    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 0):
        print("玩家赢")
    elif (player == computer):
        print("平局")
    else:
        print("电脑赢")

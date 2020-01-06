# 定义一个变量，记录循环次数

i = 0
while i < 5:
    print("第%d次" % i)
    print("实际是第%d次" % (i+1))
    print("===========")
    i +=1

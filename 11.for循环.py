# i = 0
# while i < 5:
#     print("第%d次" % i)
#     print("实际是第%d次" % (i+1))
#     print("===========")
#     i +=1

# 使用for循环
# range（x,y）表示[1,5)
for x in range(1, 5):
    print("次数：%d" % x)


# range（x）表示[0,x)---—>只是循环x次
for y in range(5):
    print("次数2：%d" % y)

# 循环字符串
name = "apple"
for z in name:
    print(z)



# continue与while的使用
# 如果执行了continue，将提前结束本次循环
i = 0
while i <= 5:
    i += 1
    if i == 2:
        continue
        # print("测试")
    print(i)
print("********")

# 与for的使用
for x in range(5):
    if x == 2:
        continue
        # print("测试")
    print(x)

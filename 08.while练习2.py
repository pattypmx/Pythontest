# 计算1-100之间偶数的和
# 偶数余数为0
# num = 1
# sum = 0   #
# 任何数加0都是自己
# while num < 101:
#     if num % 2 == 0:
#         # print(num)
#         sum += num
#     num += 1
# print("偶数之和为:%d" % sum)

# 计算所有之乘积
a = 1
result = 1  # 任何数乘以1都为自己
while a < 101:
    if a % 2 == 0:
        result *= a
    # print(result)
    a += 1
print("全部之积为：%d" % result)

# while循环和break的配合使用
# 只足满足条件，就不继续下面的循环，打印最终的值
i = 0
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print("*************")

#for循环和break的配合使用
for x in range(5):
    print(x)
    if x == 2:
        break


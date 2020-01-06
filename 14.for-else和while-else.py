# for-else
# for i in range(5):
#     print(i)
#     i += 1
# else:
#     print("else测试")
# print("****************")

# while-else
# ii = 0
# while ii < 5:
#     print(ii)
#     ii += 1
# else:
#     print("else测试")

##################################

# for-else和break结合使用，如果执行了break，else中的代码将不再执行
# for j in range(5):
#     print(j)
#     if j == 2:
#         break
#     j += 1
# else:
#     print("for执行了break测试")
# print("****************")

# while-else;break
# jj = 0
# while jj < 5:
#     print(jj)
#     if jj == 2:
#         break
#     jj += 1
# else:
#     print("while执行了break测试")

###################################

# 如果没有执行break，else中的代码将继续执行
# for
for x in range(5):
    print(x)
    if x == 22:
        break
    x += 1
else:
    print("未执行break测试")
# while
xx = 1
while xx < 5:
    print(xx)
    if xx == 22:
        break
    xx += 1
else:
    print("未执行break测试")



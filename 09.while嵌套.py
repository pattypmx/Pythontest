# 打印一个三角形
# *
# **
# ***
# ****
# *****

# 定义行cel和列row
row = 1
while row <= 5:
    cel = 1
    while cel <= row:
        print("*", end="")# 完整的打印是print("xxx", end="\n"),自动换行；如果不需要换行，就把\n去掉
        cel += 1
    print("")
    row += 1

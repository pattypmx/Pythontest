# 乘法表
# 定义行和列两个变量
i = 1  # 列
while i <= 9:
    j = 1  # 行
    while j <= i:
        print("%d * %d =%-2d" % (i, j, i*j), end="  ")  # 保留两位的位置%2d，三位就是%3d；    默认右对齐，左对齐-2
        j += 1
    print()
    i += 1

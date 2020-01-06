# 多个条件判断
score = int(input("请输入成绩："))
if score > 90 and score <= 100:
    print("成绩优秀")
elif score > 60:
    print("成绩合格")
elif score < 60:
    print("成绩不合格")
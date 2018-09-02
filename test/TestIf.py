# if语句是根据缩进来区分的，跟java不同
# 单分支
age = 15
if age >= 18:
    print("成年")
print("未成年", end="&")

# 双分支
if age >= 18:
    print("已经成年了")
else:
    print("还没有成年哦")

score = 56
if 90 < score <= 100:
    print("优秀")
elif 80 <= score <= 90:
    print("良好")
elif 60 <= score < 80:
    print("及格")
else:
    print("不及格")
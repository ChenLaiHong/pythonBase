f = open("a.txt", "r", encoding="utf-8")

# 读写操作
content = f.read()
temp = [int(i) for i in content.split(",")]
result = ""
for i in sorted(temp):
    result += str(i)+","
f.close()

f1 = open("b.txt", "w", encoding="utf-8")
f1.write(result[0:len(result)-1])
f1.close()
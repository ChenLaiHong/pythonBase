

words = input().split()
result = []
for n in words:
    n.lower()
    if n not in result:
        result.append(n)
print(result.__len__())

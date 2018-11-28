"""
编写维吉尼亚加密程序，输入秘钥key和明文，输出密文。说明一点：如果秘钥字母为大写字母，则以该字母与大写A字母的距离作为凯撒加密秘钥；
若秘钥字母为小写，则以该字母与小写a字母的距离作为凯撒加密秘钥。
"""
def find(key, document):
    while len(key) < len(document):
        key += key
    key = key[0:len(document)]
    result = ""
    for i in range(len(document)):
        if key[i].isupper():
            length = ord(key[i]) - ord("A")
        else:
            length = ord(key[i]) - ord("a")
        if document[i].isupper():
            temp = ord(document[i])+length
            if temp > 90:
                temp = temp - 26
            result += chr(temp)
        else:
            temp = ord(document[i])+length
            if temp > 122:
                temp = temp - 26
            result += chr(temp)
    return result

key = input()
document = input()
print(find(key, document))

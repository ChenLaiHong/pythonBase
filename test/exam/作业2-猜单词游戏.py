import random
HANGMAN_LIST = [
'''
 +---+
     |
     |
     |
    === 
''',
'''
 +---+
 o   |
     |
     |
    ===
''',
'''
 +---+
 o   |
 |   |
     |
    ===
''',
'''
 +---+
 o   |
/|   |
     |
    ===
''',
'''
+---+
 o  |
/|\ |
    |
   ===
''',
'''
 +---+
 o   |
/|\  |
/    |
    ===
''',
'''
 +---+
 o   |
/|\  |
/ \  |
   ===
'''
                ]
animal = ["dog", "cat", "horse", "koala", "dolphin", "lion", "monkey", "cow", "wolf", "kangaroo"]


# 填充猜中的字母
def change(suiji, kongque, word):
    temp = ""
    for i in range(len(suiji)):
        if suiji[i] == word:
            temp += suiji[i]
        else:
            temp += kongque[i]
    return temp

name = "H A N G M A N"
words = "当前空缺："
words2 = "没猜中的字母："
flag = 0

temp = ""
while True:
    suiji = animal[random.randint(0, animal.__len__()-1)]
    print(suiji)
    print(name)
    print(HANGMAN_LIST[flag])
    print(words)
    kongque = suiji.__len__()*"_"
    print(kongque)

    n = 0
    while n < len(suiji):
        word = input()
        print("你猜的下一个字母是：", word)
        if len(word) == 1 and word.isalpha():
            if word in suiji:
                print(HANGMAN_LIST[flag])
                kongque = change(suiji, kongque, word)
                print(kongque)
                print(words2, temp)
                n += 1
            else:
                flag += 1
                if flag == 6:
                    print("真不幸，你丢命了！")
                    print(HANGMAN_LIST[flag])
                    print("被猜的单词是：", suiji)
                    break
                else:
                    temp += word
                    print(HANGMAN_LIST[flag])
                    print(words)
                    kongque = change(suiji, kongque, word)
                    print(kongque)
                    print(words2, temp)
        else:
            print("输入不合法，请重新输入：")
            break
    if flag == 6:
        break
    print("你要继续玩吗？（回答yes或者no）")
    answer = input()
    if answer == "no":
        break
    else:
        flag = 0




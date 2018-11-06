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
suiji = animal[random.randint(0, animal.__len__()-1)]
print(suiji)
flag = 0
print("H A N G M A N")
print(HANGMAN_LIST[flag])
words = "当前空缺："
words2 = "没猜中的字母："
print(words)
kongque = suiji.__len__()*"_"
print(kongque)

# 填充猜中的字母
def change(suiji, kongque, word):
    temp = ""
    for i in range(len(suiji)):
        if suiji[i] == word:
            temp += suiji[i]
        else:
            temp += kongque[i]
    return temp

n = 0
temp = ""
while True:
    while n < 6:
        word = input()
        print("你猜的下一个字母是：", word)
        if len(word) == 1 and word.isalpha():
            if word in suiji:
                print(HANGMAN_LIST[flag])
                kongque = change(suiji, kongque, word)
                print(kongque)
                print(words2, temp)
            else:
                flag += 1
                if flag == 6:
                    print("真不幸，你丢命了！")
                    print(HANGMAN_LIST[flag])
                    print("被猜的单词是：", suiji)

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
        n += 1

    if flag == 6:
        break
    print("你要继续玩吗？（回答yes或者no）")
    answer = input()
    if answer == "no":
        break




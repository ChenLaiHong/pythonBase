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
gussType = [["动物", "dog", "cat", "horse", "koala", "dolphin", "lion", "monkey", "cow", "wolf", "kangaroo"],
            ["水果", "apple", "sydney", "peach", "banana", "watermelon", "grape", "orange", "strawberry", "blueberry", "cherry"],
            ["颜色", "red", "blue", "yellow", "purple", "orange", "pink", "gray", "black", "white", "brown"],
            ["交通工具", "bicycles", "trains", "buses", "cars", "subways", "planes", "cruises", "boats", "rockets", "spaceships"],
            ["家具", "TV", "fans", "refrigerators", "sofas", "tables", "stools", "cupboards", "beds", "bookshelves", "bathtubs"],
            ["学习用品", "pencils", "pens", "erasers", "rulers", "adhesive", "tapes", "dictionaries", "computers", "notebooks", "schoolbags"]]

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
error_input = 0
temp = ""
n = 0
while True:
    if error_input != 1:
        hang = random.randint(0, 5)
        suiji = gussType[hang][random.randint(0, 9)]
        print(suiji)
        print("猜测单词的类别是：", gussType[hang][0])
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
            error_input = 0
            if word in suiji:
                n += 1
                kongque = change(suiji, kongque, word)
                if kongque == suiji:
                    print("你猜对了！被猜的单词是：")
                    print(suiji)
                    print("棒棒哒！")
                    break
                else:
                    print(HANGMAN_LIST[flag])
                    print(kongque)
                    print(words2, temp)
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
            error_input = 1
            print("只能输入1个字母，请重新输入：")
            break
    if flag == 6:
        break
    if error_input != 1:
        print("你要继续玩吗？（回答yes或者no）")
        answer = input()
        if answer == "no":
            break
        else:
            flag = 0





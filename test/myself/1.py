L1 = [["hello", "world", "print"],
      ["good", "hello", "morning"]]

def createVocabList(dataset):
    temp = []
    for i in dataset:
        for j in i:
            temp.append(j)
    return list(set(temp))



# print(L1[0])
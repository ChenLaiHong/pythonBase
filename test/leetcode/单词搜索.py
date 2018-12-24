"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
"""
def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    temp = [-1, -1]
    num = 0
    result = []
    for i in word:
        flag = 0
        for j in board[flag]:
            if j == i:
                if flag == temp[0]+1 or flag == temp[1]+1:
                    temp[0], temp[1] = board[flag].index(j), flag
                    result.append(temp)
                    num += 1
                    break
        if flag < len(board):
            flag += 1
        else:
            break

    if num == len(word):
        return True
    else:
        return False



board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
print(exist(board, "ABCCED"))
print(exist(board, "SEE"))
print(exist(board, "ABCB"))
import math

import functional as F

def shape(matrix):
    if not F.is_sequence(matrix): return None

    len1 = len(matrix)
    if not (len1 > 0 and F.is_sequence(matrix[0])): return None

    len2 = len(matrix[0])

    return [len1, len2]

def matmul(X, Y):
    return [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

def matadd(X, Y):
    return [x+y for x,y in zip(X,Y)]

def sigmoid(z):
    return 1 / (1 + math.e ** -z)

def softmax2D(M, t = 1.0):
    E = F.map(M, lambda row: [math.exp(x/t) for x in row])
    total = F.sum(F.map(E, lambda row: F.sum(row)))
    return F.map(E, lambda row: [x/total for x in row])

def softmax(M, t = 1.0):
    E = [math.exp(x/t) for x in M]
    total = F.sum(E)
    return [x/total for x in E]

def argmax(M):
    max_num = -1
    max_index = -1
    for i, v in enumerate(M):
        if v > max_num:
            max_num, max_index = v, i
    return max_index

# def levenshtein_distance(first, i, second, j):
#     if i == 0:
#         return j
#     elif j == 0:
#         return i
#
#     cost = 0 if first[i - 1] == second[j - 1] else 1
#
#     return min([
#         levenshtein_distance(first, i - 1, second, j) + 1,
#         levenshtein_distance(first, i, second, j - 1) + 1,
#         levenshtein_distance(first, i - 1, second, j - 1) + cost,
#     ])
#
# print(levenshtein_distance("apple", 5 , "people", 6))

def levenshtein_distance(first, second):

    i, j = len(first), len(second)

    return j if i == 0 else \
        i if j == 0 else \
        min([
            levenshtein_distance(first[:-1], second,) + 1,
            levenshtein_distance(first, second[:-1]) + 1,
            levenshtein_distance(first[:-1], second[:-1]) + (0 if first[i - 1] == second[j - 1] else 1)
        ])

print(levenshtein_distance("apple", "people"))

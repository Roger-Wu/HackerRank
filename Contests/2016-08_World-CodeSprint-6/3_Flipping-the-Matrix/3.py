"""
Problem:    https://www.hackerrank.com/contests/world-codesprint-6/challenges/flipping-the-matrix
Language:   Python 3
Result:     Accepted
"""

q = int(input())
for caseIdx in range(1, q + 1):
    n = int(input())
    mat = []
    for r in range(2*n):
        row = list(map(int, input().strip().split(' ')))
        mat.append(row)

    maxSum = 0
    maxIdx = 2*n - 1
    for i in range(n):
        for j in range(n):
            maxSum += max([mat[i][j], mat[maxIdx - i][j], mat[i][maxIdx - j], mat[maxIdx-i][maxIdx-j]])
    print(maxSum)

"""
Problem:    https://www.hackerrank.com/contests/world-codesprint-6/challenges/bon-appetit
Language:   Python 3
Result:     Accepted
"""

n, k = map(int, input().strip().split(' '))
c = list(map(int, input().strip().split(' ')))
b = int(input())

annaCost = (sum(c) - c[k]) // 2
if b == annaCost:
    print('Bon Appetit')
else:
    print(b - annaCost)

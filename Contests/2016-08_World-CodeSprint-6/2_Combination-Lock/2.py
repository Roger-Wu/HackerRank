"""
Problem:   https://www.hackerrank.com/contests/world-codesprint-6/challenges/combination-lock
Language:   Python 3
Result:     Accepted
"""

config1 = list(map(int, input().strip().split(' ')))
config2 = list(map(int, input().strip().split(' ')))

sum = 0
for i in range(len(config1)):
    diff = abs(config1[i] - config2[i])
    if diff < 5:
        sum += diff
    else:
        sum += 10 - diff
print(sum)

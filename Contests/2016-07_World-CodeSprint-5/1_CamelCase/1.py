"""
Problem:    https://www.hackerrank.com/contests/world-codesprint-5/challenges/camelcase
Language:   Python 3
Result:     Accepted
"""

s = input().strip()

if len(s) == 0:
    print(0)
else:
    wordCount = 1
    for c in s:
        if c.isupper():
            wordCount += 1
    print(wordCount)

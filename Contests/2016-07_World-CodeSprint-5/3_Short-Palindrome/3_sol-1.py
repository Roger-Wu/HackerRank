"""
Problem:    https://www.hackerrank.com/contests/world-codesprint-5/challenges/short-palindrome
Language:   Python 3 (compiled with PyPy3)
Result:     Accepted
Description:
    A straightforward solution by Gullesnuffs in C++:
    https://www.hackerrank.com/rest/contests/world-codesprint-5/challenges/short-palindrome/hackers/Gullesnuffs/download_solution
"""

MOD = 10**9 + 7

s = input().strip()

# count how many tuples in the format so far
a = [0]*26
ab = [[0]*26 for i in range(26)]
abb = [[0]*26 for i in range(26)]
abba = [[0]*26 for i in range(26)]

for c in s:
    c2 = ord(c) - 97  # ord(c) - ord('a')
    for c1 in range(26):
        abba[c2][c1] += abb[c2][c1]
        abb[c1][c2] += ab[c1][c2]
        ab[c1][c2] += a[c1]
    a[c2] += 1

print(sum(map(sum, abba)) % MOD)

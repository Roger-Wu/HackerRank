"""
Problem:    https://www.hackerrank.com/contests/world-codesprint-5/challenges/string-construction
Language:   Python 3
Result:     Accepted
Explain:    https://www.hackerrank.com/contests/world-codesprint-5/challenges/string-construction/editorial
            To find the number of distinct characters in a string s,
            we can add all the chars in s to a set (what set(s) do)
            and see how many elements are there in the set (what len() do).
"""

n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    print(len(set(s)))

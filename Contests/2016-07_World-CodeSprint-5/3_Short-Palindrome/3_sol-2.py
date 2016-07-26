"""
Problem:    https://www.hackerrank.com/contests/world-codesprint-5/challenges/short-palindrome
Language:   Python 3
Result:     15/40  Runtime Error
Description:
    This is my first solution. Using dynamic programming.
    It takes O(n^2) time and memory.
    Since it took too much memory, Runtime Error is raised in test case 16~40.
    https://www.hackerrank.com/contests/world-codesprint-5/challenges/short-palindrome/submissions/code/6381094
    We can use much less memory by only keeping the last 3 rows of the matrix,
    but it still takes too much time.
    https://www.hackerrank.com/contests/world-codesprint-5/challenges/short-palindrome/submissions/code/6381653
Explain:
    to know how many palindromic tuples in a string "abccbab"
    if we know the numbers of palindromic tuples in "abccba" and "bccbab" and "bccba",
    then we can use the following equation to compute it:
        palinTuplesIn("abccbab")
        = tuplesInFormat( (x, x, x, <6) ) + tuplesInFormat( (>0, x, x, x) ) - tuplesInFormat( (>0, x, x, <6) )
        = palinTuplesIn("abccba") + palinTuplesIn("bccbab") - palinTuplesIn("bccba")
    With this recursive relation, we can compute palinTuplesIn("abccbab") from the bottom up.
    One more thing, if the first and the last char are the same, we still need to add
        tuplesInFormat( (0, x, x, 6) )
"""

MOD = 10**9 + 7

s = input().strip()

pairCounts = [[0]*(len(s)-length+1) for length in range(len(s)+1)]
quadCounts = [[0]*(len(s)-length+1) for length in range(len(s)+1)]

for length in range(2, len(s)+1):  # substring len
    for begin in range(len(s)-length+1):
        pairCounts[length][begin] = (
            (s[begin] == s[begin+length-1]) +
            pairCounts[length-1][begin] +
            pairCounts[length-1][begin+1] -
            pairCounts[length-2][begin+1]
        ) % MOD

        quadCounts[length][begin] = (
            (pairCounts[length-2][begin+1] if s[begin] == s[begin+length-1] else 0) +
            quadCounts[length-1][begin] +
            quadCounts[length-1][begin+1] -
            quadCounts[length-2][begin+1]) % MOD

print(quadCounts[len(s)][0])

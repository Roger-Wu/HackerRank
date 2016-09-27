"""
Problem:    https://www.hackerrank.com/contests/world-codesprint-6/challenges/bonetrousle
Language:   Python 3
Result:     Accepted
"""

def main():
    t = int(input())
    for caseIdx in range(1, t + 1):
        n, k, b = map(int, input().strip().split(' '))

        minN = (1 + b) * b // 2  # sum([1, 2, ..., b])
        maxN = (k + (k-b+1)) * b // 2  # sum([k-b+1, k-b+2, ..., k])

        if n < minN or n > maxN:
            print(-1)
        else:
            combi = findCombi(n, k, b)
            print(' '.join(map(str, combi)))

def findCombi(n, k, b):
    combi = list(range(1, b+1))
    combiSum = (1 + b) * b // 2

    if combiSum > n:  # should not happen
        return [-1]
    if combiSum == n:
        return combi

    for i in range(b):
        # push the last elements to k, k-1, ...
        combiSum -= combi[b-1-i]
        combi[b-1-i] = k-i
        combiSum += combi[b-1-i]

        if combiSum >= n:
            combi[b-1-i] = n - (combiSum - combi[b-1-i])
            return combi

if __name__ == '__main__':
    main()

"""
Problem:    https://www.hackerrank.com/contests/world-codesprint-5/challenges/longest-increasing-subsequence-arrays
Language:   Python 3 (compiled with PyPy3)
Result:     Accepted
Explain:    https://www.hackerrank.com/contests/world-codesprint-5/challenges/longest-increasing-subsequence-arrays/editorial
    It's important to precalculate factorials and their multiplicative inverses.
"""

MOD = 10**9 + 7

def main():
    # precalculate
    fact, invFact = calcFactorials(5*10**5)

    t = int(input())
    for caseIdx in range(1, t + 1):
        m, n = map(int, input().strip().split(' '))

        # precalculate
        powN, powN_1 = calcPowers(m, n)

        # solve
        result = 0
        for x in range(m - n + 1):
            # result += combinations(m-x-1, n-1) * n**x * (n-1)**(m-n-x)
            result += fact[m-x-1] * invFact[m-x-n] * invFact[n-1] * powN[x] * powN_1[m-n-x]

        print(result % MOD)

def calcPowers(m, n):
    # build n**x and (n-1)**x
    powN = [1] * (m - n + 1)
    powN_1 = [1] * (m - n + 1)
    for i in range(1, m - n + 1):
        powN[i] = powN[i-1] * n % MOD
        powN_1[i] = powN_1[i-1] * (n-1) % MOD
    return powN, powN_1

def calcFactorials(m):
    # build (x! % MOD) and multiplicative inverse of (x! % MOD)
    fact = [1] * (m+1)
    for i in range(2, m+1):
        fact[i] = (fact[i-1] * i) % MOD
    invFact = [modinv(x, MOD) for x in fact]
    return fact, invFact

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

if __name__ == '__main__':
    main()

"""
Problem:    https://www.hackerrank.com/contests/world-codesprint-6/challenges/abbr
Language:   Python 3
Result:     Accepted
"""

def main():
    q = int(input())
    for caseIdx in range(1, q + 1):
        a = input()
        b = input()

        if checkConvertable(a, b):
            print('YES')
        else:
            print('NO')

def checkConvertable(a, b):
    if len(b) == 0:
        if len(a) == 0:
            return True
        return a.islower()  # is all lowercase

    for ai in range(len(a)):
        if a[ai].isupper():
            if a[ai] != b[0]:
                return False
            else:
                return checkConvertable(a[ai+1:], b[1:])
        else:  # elif a[ai].islower():
            if a[ai].upper() == b[0]:
                if checkConvertable(a[ai+1:], b[1:]):
                    return True
                # else:
                #     continue

    return False

if __name__ == '__main__':
    main()

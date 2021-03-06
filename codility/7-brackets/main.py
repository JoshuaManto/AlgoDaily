"""
    same as lc20

    Time    O(n)
    Space   O(n)
    Result  100/100 https://app.codility.com/demo/results/training68UH55-79D/
"""


def solution(S):
    # write your code in Python 3.6
    stack = []
    m = {
        ']': '[',
        ')': '(',
        '}': '{'
    }
    for c in S:
        if c == '[' or c == '(' or c == '{':
            stack.append(c)
        else:
            if len(stack) == 0:
                return 0
            if m[c] == stack[-1]:
                stack.pop()
            else:
                return 0
    return 1 if len(stack) == 0 else 0

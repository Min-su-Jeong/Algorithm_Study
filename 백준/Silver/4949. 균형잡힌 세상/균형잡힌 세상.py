import sys
input = lambda: sys.stdin.readline().rstrip()

def check(s: str):
    stk = []
    for c in s:
        if c == ')':
            if not stk or stk[-1] == '[':
                return False
            else:
                stk.pop()

        if c == ']':
            if not stk or stk[-1] == '(':
                return False
            else:
                stk.pop()

        if c == '(' or c == '[':
            stk.append(c)

    if stk: return False
    else: return True

while True:
    s = input()
    if s == ".":
        break

    ret = check(s)
    if ret:
        print("yes")
    else:
        print("no")
import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    s = input()
    if s == ".":
        break

    stk = []
    flag = True
    for c in s:
        if c == ")":
            if not stk or stk[-1] == "[":
                flag = False
                break
            else:
                stk.pop()

        if c == "]":
            if not stk or stk[-1] == "(":
                flag = False
                break
            else:
                stk.pop()

        if c == "(" or c == "[": stk.append(c)
    
    if flag and not stk: print("yes")
    else: print("no")
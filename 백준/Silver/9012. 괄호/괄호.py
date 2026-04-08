N = int(input())

for _ in range(N):
    stk = []
    string = input()

    for s in string:
        if stk and stk[-1] == "(" and s == ")":
            stk.pop()
        else:
            stk.append(s)

    if stk:
        print("NO")
    else:
        print("YES")
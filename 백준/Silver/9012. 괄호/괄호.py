def check(s: str):
    stk = []
    for c in s:
        if stk and stk[-1] == '(' and c == ')':
            stk.pop()
        else: stk.append(c)
    
    return len(stk) == 0

if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        s = input()

        if check(s): print("YES")
        else: print("NO")
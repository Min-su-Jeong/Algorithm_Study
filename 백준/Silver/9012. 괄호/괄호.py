def check(s: str):
    stk = []
    for c in s:
        if c == '(': stk.append(c)
        else:
            if stk: stk.pop()
            else: return False
    
    return len(stk) == 0

if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        s = input()

        if check(s): print("YES")
        else: print("NO")
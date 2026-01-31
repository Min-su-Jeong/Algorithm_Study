N = int(input())

ret = 0
for _ in range(N):
    s = input()
    stk = []

    for ch in s:
        if stk and stk[-1] == ch:
            stk.pop()
            continue
        
        stk.append(ch)
    
    if not stk: ret += 1
    
print(ret)
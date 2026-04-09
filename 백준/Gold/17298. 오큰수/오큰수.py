N = int(input())
num = list(map(int, input().split()))

stk = []
ret = [-1] * N

for i in range(N):
    while stk and num[stk[-1]] < num[i]:
        ret[stk[-1]] = num[i] 
        stk.pop()
    stk.append(i)

print(*ret)
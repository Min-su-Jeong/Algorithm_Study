n = int(input())
stack, res = [], []
cur, flag = 1, 1

for _ in range(n):
    num = int(input())
    
    # stack push
    while cur <= num:
        stack.append(cur)
        res.append('+')
        cur += 1
    
    # stack pop
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    
    # impossible
    else:
        flag = 0

if flag == 0:
    print('NO')
else:
    for i in res:
        print(i)
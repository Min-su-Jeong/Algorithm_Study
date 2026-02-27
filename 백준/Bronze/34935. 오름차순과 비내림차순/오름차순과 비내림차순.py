N = int(input())
arr = list(map(int, input().split()))

flag = True
num = arr[0]
for i in range(1, N):
    if num >= arr[i]:
        flag = False
        break
    
    num = arr[i]
    
if flag: print(1)
else: print(0)
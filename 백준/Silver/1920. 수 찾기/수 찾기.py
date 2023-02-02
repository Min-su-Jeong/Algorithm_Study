n = int(input())
nlist = sorted(list(map(int, input().split())))
m = int(input())
mlist = list(map(int, input().split()))

# 이분 탐색
for i in mlist:
    s, e = 0, n-1
    
    while s <= e:
        mid = (s+e) // 2
        if i == nlist[mid]:
            print(1)
            break            
        elif i > nlist[mid]:
            s = mid + 1        
        elif i < nlist[mid]:
            e = mid - 1
    
    else:
        print(0)
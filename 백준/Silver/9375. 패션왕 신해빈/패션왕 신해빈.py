T = int(input())

while T:
    mp = {}
    n = int(input())
    for _ in range(n):
        _, acc = input().split()
        mp[acc] = mp.get(acc, 0) + 1

    ret = 1
    for c in mp.values():
        ret *= (c+1)
    
    print(ret-1)

    T -= 1
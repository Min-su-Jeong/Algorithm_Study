t = int(input())

for _ in range(t):
    ret = 1
    clothes = {}

    n = int(input())
    for _ in range(n):
        _, c = input().split()
        if not c in clothes:
            clothes[c] = 1
        else:
            clothes[c] += 1

    for c in clothes.values():
        ret *= (c+1)
        
    ret -= 1

    print(ret)
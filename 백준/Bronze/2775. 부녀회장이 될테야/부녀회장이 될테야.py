for _ in range(int(input())):
    k, n = [int(input()) for _ in range(2)]
    p = [i for i in range(1, n+1)]
    
    for __ in range(k):
        for y in range(1, n):
            p[y] += p[y-1]
    print(p[-1])
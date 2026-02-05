def solution(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    k = min(k, n - k)
    
    ret = 1
    for i in range(k):
        ret = ret * (n - i) // (i + 1)
    
    return ret

T = int(input())

while T:
    N, M = map(int, input().split())
    print(solution(M, N))
    T -= 1
"""
1.전략
- 백트래킹

2.시간복잡도
O(N^2) = 8 * 8 = 64
=> 1초 내 가능
"""
def backTracking(curNum):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(curNum, N+1):
        arr.append(i)
        backTracking(curNum)
        curNum += 1
        arr.pop()
        
N, M = map(int, input().split())
arr = []

backTracking(1)
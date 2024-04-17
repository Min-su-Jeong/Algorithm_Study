"""
1.전략
- 백트래킹
- 중복 허용가능한 수열
- 방문 여부(visited) 확인 필요 X

2.시간복잡도
O(N^2) = 8 * 8 = 64
=> 1초 내 가능
"""
def backTracking():
    if len(arr) == M:
        print(*arr)
        return
    
    for i, num in enumerate(nums):
        arr.append(num)
        backTracking()
        arr.pop()
    
arr = []
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

backTracking()
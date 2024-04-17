"""
1.전략
- 백트래킹
- n번째 수보다 n+1번째 수가 더 커야하며 뒤에 있어야 함.
- 중복 가능한 수열

2.시간복잡도
O(N^2) = 8 * 8 = 64
=> 1초 내 가능
"""
def backTracking(curNum: int):
    if len(arr) == M:
        print(*arr)
        return
    
    for i, num in enumerate(nums):
        if curNum <= num:
            arr.append(num)
            backTracking(num)
            arr.pop()
    
arr = []
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

backTracking(0)
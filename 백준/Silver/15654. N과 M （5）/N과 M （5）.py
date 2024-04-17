"""
1.전략
- 백트래킹
- 15652번과의 차이점: 1씩 증가가 아닌 입력 값들에 대한 수열 문제

2.시간복잡도
O(N^2) = 8 * 8 = 64
=> 1초 내 가능
"""
def backTracking():
    if len(arr) == M:
        print(*arr)
        return
    
    for i, num in enumerate(nums):
        if not visited[i]:
            arr.append(num)
            visited[i] = True
            backTracking()
            arr.pop()
            visited[i] = False
        
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = []
visited = [False] * len(nums)

backTracking()
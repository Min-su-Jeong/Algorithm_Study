"""
1.전략
- 백트래킹
- 15654번과의 차이점: n번째 수보다 n+1번째 수가 더 커야하며 뒤에 있어야 함.
- 비교하기 위해 현재 숫자 값을 가지는 변수를 추가

2.시간복잡도
O(N^2) = 8 * 8 = 64
=> 1초 내 가능
"""
def backTracking(curNum: int):
    if len(arr) == M:
        print(*arr)
        return
    
    for i, num in enumerate(nums):
        if not visited[i] and curNum < num:
            arr.append(num)
            visited[i] = True
            backTracking(num)
            arr.pop()
            visited[i] = False
        
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = []
visited = [False] * len(nums)

backTracking(0)
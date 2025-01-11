"""
1.전략
- DFS(Depth-First Search)
- 로마숫자의 조합은 중복 허용, 
- 로마숫자의 합이 중복되지 않기 위해 Set 함수 사용
- 이를 순회하며 탐색하고자 DFS 알고리즘 사용

2.시간 복잡도
- 시간 제한: 2초
- O(N^4)
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())

# Variables
curNum = 0
arr = [0] * 1001
roma = [1, 5, 10, 50]

# Solution
def dfs(depth: int, curIdx: int):
    global curNum

    if depth == N:
        arr[curNum] = 1
        return

    for i in range(curIdx, 4):
        curNum += roma[i]
        dfs(depth+1, i)
        curNum -= roma[i]
        
# Main
dfs(0, 0)

# Output
print(sum(arr))
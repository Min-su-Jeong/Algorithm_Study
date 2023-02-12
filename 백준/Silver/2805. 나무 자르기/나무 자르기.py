import sys

input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))
s, e = 1, max(tree)

while s <= e: # 이분 탐색 사용
    mid = (s+e) // 2
    log = sum(i-mid if i > mid else 0 for i in tree)
            
    if log >= m:
        s = mid + 1
    else:
        e = mid - 1
        
print(e)
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))
s, e = 1, max(tree)

while s <= e: # 이분 탐색 사용
    log = 0 # 벌목된 나무 총합
    mid = (s+e) // 2
    
    for i in tree:
        if i > mid:
            log += i - mid
            
    if log >= m:
        s = mid + 1
    else:
        e = mid - 1
        
print(e)
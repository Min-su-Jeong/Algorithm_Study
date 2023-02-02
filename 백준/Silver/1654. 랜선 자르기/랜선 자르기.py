import sys

k, n  = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
s, e = 1, max(lan)

# 이분 탐색
while s <= e:
    mid = (s+e) // 2 # 중간값 구하기
    cnt = sum([i//mid for i in lan]) # 잘라지는 개수의 합 구하기
    
    if cnt >= n: # 자른 개수가 필요한 개수보다 많아지면 => 더 크게 자르기
        s = mid + 1
    else: # 자른 개수가 필요한 개수보다 적어지면 => 더 작게 자르기
        e = mid - 1
        
print(e)
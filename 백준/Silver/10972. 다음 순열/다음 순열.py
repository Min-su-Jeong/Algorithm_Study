"""
1.전략
- 브루트포스
- 1. 작은 수가 앞에 배치되어 있는지 확인(뒤에서부터 탐색 시작)
- 2. 인덱스 값이 앞에 값보다 큰 값이 있다면 그 값과 Swap
- 3. Swap을 반복 후, i에 해당하는 인덱스부터 오름차순 정렬 + 이어 붙이기

2. 시간복잡도
- O(N^2) = 10,000 ^ 2 = 100,000,000 (Worst Case)
  => 1초 이내 가능
"""
import sys; 
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    # 뒷 값이 앞 값보다 큰 경우
    if arr[i-1] < arr[i]:
        for j in range(N-1, 0, -1):
            # i-1 인덱스 값이 j 인덱스보다 작은 경우
            if arr[i-1] < arr[j]:
                # Swap
                arr[i-1], arr[j] = arr[j], arr[i-1]
                # index: i 이후 값들을 오름차순 정렬 후 리스트화 
                arr = arr[:i] + sorted(arr[i:])
                print(*arr)
                exit()
    
# 마지막 순열인 경우
print(-1)
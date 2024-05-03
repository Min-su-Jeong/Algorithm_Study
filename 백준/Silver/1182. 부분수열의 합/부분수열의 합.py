"""
1.전략
- 백트래킹(Back tracking)
- 부분 수열을 찾아야하므로 조합이 필요하다고 판단
- 조합 + 조건에 맞는 경우를 찾기 위해서 수열을 순회하면서 부합하는 경우 결과+1

2.시간 복잡도
- O(2^N) = 2 ^ 20 = 1,048,576 (Worst case)
  => 2초 이내 가능
"""
import sys; input = sys.stdin.readline

def backTracking(start_idx: int):
    global res

    # 합이 S인 경우 & 부분 수열의 길이가 1 이상인 경우
    if sum(arr) == S and len(arr) > 0:
        res += 1
    
    # 순회(중복 X) -> start_idx부터 시작
    for i in range(start_idx, N):
        arr.append(seq[i])
        backTracking(i+1)
        arr.pop()

# 입력
N, S = map(int, input().split())
seq = list(map(int, input().split()))

# 필요한 변수 선언 및 초기화
res = 0
arr = []

# 함수 실행
backTracking(0)

# 출력
print(res)
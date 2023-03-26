import math
def composite(x):                             # 합성수 판별 함수
    for i in range(2, int(math.sqrt(x)) + 1): # 시간 복잡도: O(root(N))
        if x % i == 0:                        # x가 해당 수로 
            return True                       # 나누어 떨어진다면, 합성수
    return False                              # 나누어 떨어지지 않으면, 소수

def solution(n):
    return sum(1 for i in range(2, n+1) if composite(i))
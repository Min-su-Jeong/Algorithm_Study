# DP를 통한 해결 => 점화식 사용
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solution(n-1) + solution(n-2) + solution(n-3)

for i in range(int(input())):
    n = int(input())
    print(solution(n))
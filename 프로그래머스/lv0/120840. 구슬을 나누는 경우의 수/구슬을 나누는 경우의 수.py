# 팩토리얼 함수 이용
def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def solution(balls, share):
    return fact(balls) // fact(share) // fact(balls-share) # 이항계수 구하여 반환
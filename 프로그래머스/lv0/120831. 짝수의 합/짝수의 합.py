def solution(n):
    ans = 0
    for i in range(n+1): # n 이하의 수까지 반복
        if i % 2 == 0:   # 해당 숫자가 짝수인 경우
            ans += i     # 누적 합
            
    return ans
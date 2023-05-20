def solution(a, b, n):
    res = 0 # 결과를 저장하는 변수
    
    while n >= a:      # 콜라를 받기 위해 마트에 주어야 하는 병 수보다 같거나 큰 경우
        remain = n % a # 남아있는 병 수
        n = (n//a) * b # 마트에서 받은 콜라의 수
        res += n       # 받는 콜라 병 수 누적 합
        n += remain    # 다음에 사용할 남아있는 병 수
        
    return res
def solution(price, money, count):
    # 부족한 금액 계산
    res = sum([price * i for i in range(1, count+1)]) - money
    
    # 금액이 부족한 경우는 res 값, 부족하지 않은 경우 0 반환
    return res if res > 0 else 0
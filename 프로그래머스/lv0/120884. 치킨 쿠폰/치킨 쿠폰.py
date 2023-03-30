def solution(chicken):
    res = 0
    
    while chicken >= 10:           # 치킨이 10마리 이상일 때 동안
        eat = chicken // 10        # 쿠폰으로 먹은 치킨의 수
        res += eat                 # 최대 서비스 치킨의 수
        chicken = chicken%10 + eat # 잔여 쿠폰의 수
        
    return res
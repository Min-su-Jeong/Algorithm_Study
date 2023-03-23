def solution(price):
    dc_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1} # 할인 비율 정의
    for dc_price, dc_rate in dc_rates.items():                # 딕셔너리 형태로 값 들고오기
        if price >= dc_price:                                 # 구매한 옷 가격이 조건에 따라
            return int(price * dc_rate)                 # 할인 비율을 적용한 가격 반환
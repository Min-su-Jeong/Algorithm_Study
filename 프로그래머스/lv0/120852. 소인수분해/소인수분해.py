def solution(n):
    i, res = 2, []
    while i <= n:            # 2 ~ (n-1)까지 반복
        if n % i == 0:       # n을 i로 나누어 떨어지면
            res.append(i) # 소인수분해 판별(리스트에 추가)
            n //= i          # n을 i로 나눈 몫을 다시 n으로 지정
        else:                # 아닌 경우
            i += 1           # i+1
            
    return list(dict.fromkeys(res)) # 중복 제거 및 순서 유지 후 반환
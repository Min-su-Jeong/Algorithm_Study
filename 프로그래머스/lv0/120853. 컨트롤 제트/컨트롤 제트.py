def solution(s):
    res, sp = 0, s.split(" ")
    for i in range(len(sp)):
        if sp[i] == 'Z':        # 'Z'가 나오는 경우,
            res -= int(sp[i-1]) # 바로 전에 더했던 숫자 빼기
        else:                   # 아닌 경우,
            res += int(sp[i])   # 숫자 더하기
            
    return res

def solution(arr):
    tmp = -1
    res = []
    for a in arr:
        if a != tmp: # 숫자가 연속적이지 않으면
            tmp = a  # tmp를 a 값으로 정의
            res.append(tmp) # res에 tmp 값 추가
        else:
            pass
        
    return res
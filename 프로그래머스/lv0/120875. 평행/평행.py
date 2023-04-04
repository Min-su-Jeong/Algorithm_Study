# 기울기 계산 함수
def gradient(d1,d2):
    return (d2[1] - d1[1]) / (d2[0] - d1[0])

def solution(dots):
    res = 0
    # 3가지 경우의 수에 대한 평행 여부 확인
    if gradient(dots[0],dots[1]) == gradient(dots[2],dots[3]):
        res = 1
    if gradient(dots[0],dots[2]) == gradient(dots[1],dots[3]):
        res = 1
    if gradient(dots[0],dots[3]) == gradient(dots[1],dots[2]):
        res = 1
            
    return res
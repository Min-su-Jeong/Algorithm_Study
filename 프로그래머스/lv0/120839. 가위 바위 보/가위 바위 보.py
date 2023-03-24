def solution(rsp):
    win = {"2": "0", "0": "5", "5": "2"}      # 딕셔너리 사용
    return ''.join(win[i] for i in list(rsp)) # key 값에 대해서 이기는 경우의 value 값 반환
    

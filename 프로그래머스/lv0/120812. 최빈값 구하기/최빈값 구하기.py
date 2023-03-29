def solution(array):
    while len(array) != 0:                 # 배열의 길이가 0이 아닐 때까지 반복
        for i, a in enumerate(set(array)): # 배열 숫자 중복 제거 후 반복
            array.remove(a)                # 배열의 a 요소 제거
        if i == 0:                         # i가 0인 경우
            return a                       # a 반환
    return -1
def solution(absolutes, signs):
    # signs 값에 따른 양수, 음수 변환 후 리스트로 만들기, 리스트의 합 반환
    return sum([i if signs[idx] else -i for idx, i in enumerate(absolutes)])
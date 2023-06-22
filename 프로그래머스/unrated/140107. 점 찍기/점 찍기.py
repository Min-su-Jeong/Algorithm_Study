def solution(k, d):
    # x를 기준으로 0부터 d까지 k만큼 늘려가며, y를 세기
    return sum([(d**2 - i**2) ** 0.5 // k + 1 for i in range(0, d+1, k)])

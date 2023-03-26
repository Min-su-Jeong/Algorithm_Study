def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0 # 오름차순 정렬을 통해 같은지 여부를 판단하여 반환
        
def solution(participant, completion):
    # 두 목록을 정렬
    participant.sort()
    completion.sort()

    # 정렬된 두 목록을 비교
    for p, c in zip(participant, completion):
        if p != c:
            return p  # 참가자와 완주자가 다르면 참가자가 완주하지 못한 선수

    # 모든 완주자가 같다면, 마지막 참가자가 완주하지 못한 선수
    return participant[-1]
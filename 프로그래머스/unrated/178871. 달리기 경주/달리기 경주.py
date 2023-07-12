def solution(players, callings):
    # 딕셔너리로 변환
    res = {player:i for i, player in enumerate(players)}
    
    # callings 요소 하나씩 반환
    for call in callings: 
        # 불린 선수이름의 인덱스 값
        rank = res[call]
        # 선수 순위 swap
        res[call] -= 1
        res[players[rank-1]] += 1
        # 선수 이름 swap
        players[rank-1], players[rank] = players[rank], players[rank-1]
        
    return players
def solution(participant, completion):
    player = {}
    tmp = 0
    for p in participant:
        player[hash(p)] = p
        tmp += int(hash(p))
        
    for c in completion:
        tmp -= int(hash(c))
        
    ret = player[tmp]
    
    return ret
        
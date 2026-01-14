def solution(lottos, win_nums):
    ret = []
    rankDict = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    zeroCnt = lottos.count(0)
            
    minMatch = len(set(lottos) & set(win_nums))
    maxMatch = minMatch + zeroCnt
    
    ret.append(rankDict[maxMatch])
    ret.append(rankDict[minMatch])
    
    return ret
    
    
    
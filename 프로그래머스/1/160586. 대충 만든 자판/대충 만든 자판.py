def solution(keymap, targets):
    ret = []
    keyDict = {}
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            ch = keymap[i][j]
            if ch in keyDict.keys():
                keyDict[ch] = min(keyDict[ch], j+1)
            else:
                keyDict[ch] = j+1
                
    for target in targets:
        cnt = 0
        for ch in target:
            if ch in keyDict.keys():
                cnt += keyDict[ch]
            else:
                cnt = -1
                break
                
        ret.append(cnt)
        
    return ret
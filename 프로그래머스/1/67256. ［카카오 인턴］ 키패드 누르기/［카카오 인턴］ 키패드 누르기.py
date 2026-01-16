def solution(numbers, hand):
    ret = ''
    pad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1)
    }
    clickL = [1, 4, 7]
    clickR = [3, 6, 9]
    lPos = (3, 0)
    rPos = (3, 2)
    
    for n in numbers:
        if n in clickL:
            ret += 'L'
            lPos = pad[n]
        elif n in clickR:
            ret += 'R'
            rPos = pad[n]
        else:
            lDist = abs(lPos[0] - pad[n][0]) + abs(lPos[1] - pad[n][1])
            rDist = abs(rPos[0] - pad[n][0]) + abs(rPos[1] - pad[n][1])
            
            if lDist < rDist:
                ret += 'L'
                lPos = pad[n]
            elif lDist > rDist:
                ret += 'R'
                rPos = pad[n]
            else:
                if hand == "right":
                    ret += 'R'
                    rPos = pad[n]
                elif hand == "left":
                    ret += 'L'
                    lPos = pad[n]
    return ret
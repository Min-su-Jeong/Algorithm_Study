def solution(absolutes, signs):
    ret = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            ret += num
        else:
            ret -= num
            
    return ret
            
def getDivisor(n, limit , power):
    cnt = 0
    for i in range(1, int(n**(1/2))+1):
        if n%i == 0:
            if i == n//i:
                cnt += 1
            else:
                cnt += 2
        if cnt > limit:
            return power
    return cnt

def solution(number, limit, power):
    cnt_list = []
    
    for i in range(1, number+1):
        cnt_list.append(getDivisor(i, limit, power))
        
    return sum(cnt_list)

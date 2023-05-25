def solution(d, budget):
    s = 0
    lst = []
    for i in sorted(d):
        s += i
        if s <= budget:
            lst.append(i)
            
    return len(lst)
        
        
            
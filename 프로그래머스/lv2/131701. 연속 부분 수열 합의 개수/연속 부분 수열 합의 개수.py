def solution(elements):
    cycle = elements * 2
    s = set()
    for i in range(len(elements)):
        for j in range(len(elements)):
            s.add(sum(cycle[i:i+j]))
            
    return len(s)
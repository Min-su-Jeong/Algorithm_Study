def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        x = queue.pop(0)
        if any(x[1] < q[1] for q in queue):
            queue.append(x)
        else:
            answer += 1
            if x[0] == location:
                return answer
def solution(X, Y):
    answer = []
    
    for i in (set(X) & set(Y)):
        for j in range(min(X.count(i), Y.count(i))):
            answer.append(i)
    
    answer.sort(reverse=True)
    
    if not len(answer):
        return "-1"
    elif answer[0] == "0":
        return "0"
    
    return ''.join(answer)

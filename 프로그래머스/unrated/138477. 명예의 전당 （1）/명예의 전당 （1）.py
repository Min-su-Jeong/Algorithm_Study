def solution(k, score):
    stack = []
    res = []
    for s in score:         # score의 요소 하나씩 꺼내기
        if len(stack) < k:  # stack의 길이가 k보다 작은 경우
            stack.append(s) # 요소 삽입
        else: 
            if s > stack[-1]:   # stack에서 가장 작은 값보다 s가 큰 경우
                stack.pop()     # 가장 작은 값 제거
                stack.append(s) # stack에 s 삽입
                
        stack = sorted(stack, reverse=True) # 내림차순 정렬
        res.append(stack[-1]) # 결과값에 stack에서 가장 작은 값 추가
    
    return res
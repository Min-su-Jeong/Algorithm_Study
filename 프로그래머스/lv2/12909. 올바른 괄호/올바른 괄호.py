def solution(s):
    stack = []
    for c in s:
        if c == '(':         # '('가 나올 때까지 stack에 삽입
            stack.append(c)
        else:                # ')'가 나온 경우
            if stack:        # stack이 차있으면 하나씩 비우기
                stack.pop()
            else:            # stack이 비워져 있는 경우
                return False # 짝이 맞지 않으므로 False 반환
    
    if stack:                # 만약, stack에 요소가 남아 있는 경우 False 반환
        return False
    else:                    # 그렇지 않은 경우 True 반환
        return True
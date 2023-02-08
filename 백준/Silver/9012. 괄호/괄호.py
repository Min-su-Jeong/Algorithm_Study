n = int(input())

for _ in range(n):
    stack = []
    for s in input():
        if s == '(':
            stack.append('(')
        else: # ')' 인 경우
            if stack: # stack에 괄호가 있는 경우
                stack.pop()
            else: # stack에 괄호가 없는 경우
                print('NO')
                break
    else: # for문에서 break가 발생하지 않은 경우
        if not stack:
            print('YES')
        else:
            print('NO')
import sys

while 1:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break
        
    stack = []
    for i in s:
        if i not in '()[]':
            continue
        if i == '(' or i == '[':
            stack.append(i)
        elif (i == ')' and stack and stack[-1] == '(') or (i == ']' and stack and stack[-1] == '['):
            stack.pop()
        else:
            stack.append(-1)
            break
            
    if stack:
        print('no')
    else:
        print('yes')
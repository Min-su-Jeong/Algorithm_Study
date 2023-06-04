def solution(numbers):
    stack = []
    res = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            res[stack.pop()] = numbers[i]
        stack.append(i)
        
    return res
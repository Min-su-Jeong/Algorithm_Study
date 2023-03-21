def solution(numbers):
    n = sorted(numbers)
    return n[-1] * n[-2]
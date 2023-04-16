def solution(x):
    return False if x % sum([int(x) for x in str(x)]) else True
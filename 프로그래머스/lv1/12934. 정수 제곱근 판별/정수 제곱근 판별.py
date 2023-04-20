def solution(n):
    res = 0
    num = n ** 0.5

    if num == int(num):
        res = (num+1) ** 2
    else:
        res = -1

    return res
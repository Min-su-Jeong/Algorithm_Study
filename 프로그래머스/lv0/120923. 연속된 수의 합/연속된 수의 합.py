def solution(num, total):
    ans = []
    n = (total - sum(range(num+1)))//num
    return [i+1+n for i in range(num)]

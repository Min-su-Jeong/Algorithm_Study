from collections import Counter

def solution(k, tangerine):
    cnt = 1
    for c in Counter(tangerine).most_common():
        if k-c[1] <= 0:
            return cnt
        else:
            k = k-c[1]
            cnt += 1
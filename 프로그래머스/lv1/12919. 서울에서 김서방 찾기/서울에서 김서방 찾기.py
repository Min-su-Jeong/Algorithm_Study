def solution(seoul):
    return ''.join(["김서방은 %d에 있다" % i for i, s in enumerate(seoul) if "Kim" == s])

             
def solution(c):
    if (n := c[1] - c[0]) == (c[2] - c[1]): # 등차수열인 경우
        return c[-1] + n                    # 다음에 올 숫자 = 차이(n)만큼 증가
    else:                                   # 등비수열인 경우
        return c[-1] * (c[1]/c[0])          # 다음에 올 숫자 = 비율만큼 증가
                                            
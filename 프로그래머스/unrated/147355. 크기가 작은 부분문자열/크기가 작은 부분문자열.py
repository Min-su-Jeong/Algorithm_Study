def solution(t, p):
    # p의 길이만큼 부분문자열 생성 후, 크기를 비교하여 작거나 같은 것이 나오는 횟수 합 반환
    return sum(1 for i in range(len(t)-len(p)+1) if int(p) >= int(t[i:i+len(p)]))
            
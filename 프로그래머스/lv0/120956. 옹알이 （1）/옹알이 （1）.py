def solution(babbling):
    ans = 0
    word = ["aya", "ye", "woo", "ma"] # 4가지 발음 리스트
    for b in babbling:                # babbling 문자열 요소 반복
        for w in word:                # 4가지 발음 요소 반복
            if w * 2 not in b:        # 연속된 발음이 아닌 경우
                b = b.replace(w, ' ') # 4가지 발음 중 일치하는 부분을 공백('')으로 치환
        if b.strip() == '':           # 치환된 문자가 공백('')인 경우
            ans += 1                  # 발음 가능한 문자로 판단
    return ans
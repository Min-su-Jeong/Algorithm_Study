def solution(s):
    res = []
    s = s.split(' ')

    for i in range(len(s)):
        result = ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                result += s[i][j].upper()
            else:
                result += s[i][j].lower()

        res.append(result)

    return ' '.join(res)
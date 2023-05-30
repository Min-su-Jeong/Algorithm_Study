def solution(n, arr1, arr2):
    res = []
    for a, b in zip(arr1, arr2):
        # 2진수 or 연산, n 길이로 문자열 앞에 0 채우기 
        s = str(bin(a | b)[2:]).zfill(n)
        # 문자열 치환(1인 경우 #, 0인 경우 공백)
        res.append(s.replace('1', '#').replace('0', ' '))
        
    return res
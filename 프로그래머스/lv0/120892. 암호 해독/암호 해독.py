def solution(cipher, code):
    return ''.join([cipher[i] for i in range(code-1, len(cipher), code)]) # code 배수에 해당되는 인덱스를 뽑아서 반환
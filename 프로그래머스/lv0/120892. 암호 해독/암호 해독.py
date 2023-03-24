def solution(cipher, code):
    return cipher[code-1::code] # code 배수에 해당되는 인덱스를 뽑아서 반환
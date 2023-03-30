def solution(numbers):
    # 알파벳 -> 숫자로 변환할 수 있는 딕셔너리 정의
    alpha = {'zero' : 0, 'one':1, 'two':2, 'three' : 3, 'four':4, 
            'five':5,'six' : 6, 'seven' : 7, 'eight':8,'nine':9}
    
    # numbers 문자열에서 각 알파벳에 해당되는 문자열->숫자로 치환하기
    for k, v in alpha.items():
        numbers = numbers.replace(k, str(v))
        
    # 결과 반환
    return int(numbers)
def valid(e):
    e = e.replace('=', '==')
    return eval(e) # 매개변수로 받은 식을 문자열로 받아, 실행시킴(식 계산의 판정 여부 반환)

def solution(quiz):
    return ["O" if valid(e) else "X" for e in quiz] # 옳은 수식인 경우 'O', 옳지 않은 수식인 경우 'X'
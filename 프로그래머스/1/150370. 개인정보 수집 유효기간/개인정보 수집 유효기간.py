# 날짜 -> 일 수로 변환하기
# 일 수 비교 -> 유효기간 지난 날짜를 리스트에 삽입

def calcPeriod(period):
    y, m, d = map(int, period.split('.'))
    return y * 12 * 28 + m * 28 + d
    
def solution(today, terms, privacies):
    ret = []
    
    termDict = {}
    for term in terms:
        pType, period = term.split()
        termDict[pType] = int(period) * 28
    
    
    today = calcPeriod(today)
    for i, p in enumerate(privacies):
        period, pType = p.split()
        period = calcPeriod(period)
        period += termDict[pType]
    
        if today >= period:
            ret.append(i+1)
            
    return ret
    
N = int(input())
A = list(map(int, input().split())) + [0, 0]
res = 0

def buyRamen(i, minVal, cost):
    global A

    A[i] -= minVal
    A[i+1] -= minVal
    if cost == 7: 
        A[i+2] -= minVal

    return cost * minVal

for i in range(N):
    if A[i+1] > A[i+2]:
        # 2개 연속 찾기
        minVal = min(A[i], A[i+1]-A[i+2])
        res += buyRamen(i, minVal, 5)

        # 3개 연속 찾기
        minVal = min(A[i], A[i+1], A[i+2])
        res += buyRamen(i, minVal, 7)

    else:
        # 3개 연속 찾기
        minVal = min(A[i], A[i+1], A[i+2])
        res += buyRamen(i, minVal, 7)

        # 2개 연속 찾기
        minVal = min(A[i], A[i+1])
        res += buyRamen(i, minVal, 5)

    res += A[i] * 3
    A[i] = 0

print(res)
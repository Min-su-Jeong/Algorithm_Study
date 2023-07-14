import sys
input = sys.stdin.readline

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    
n = int(input())
if not n:
    print(0)
    
else:
    # n의 15% 값 찾기 
    cut = my_round(n * 0.15)
    
    # 난이도 의견 입력받은 후 오름차순 정렬
    op = [int(input()) for _ in range(n)]
    op = sorted(op)[cut:n-cut]
    
    result = my_round(sum(op) / len(op))
    print(result)
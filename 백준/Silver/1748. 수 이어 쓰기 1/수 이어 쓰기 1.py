"""
1.전략
- 수학, 구현
- 시간 제한이 짧으므로 하나의 수식이 필요해 보임
- 규칙 찾기
  "예제2. 15 = 9 * 1 + (15-10+1) * 2 = 21"
  "예제3. 120 = (9-0) * 1 + (99-9) * 2 + (120-99) * 3 = 252
- Input = a, len(a) = length 라고 가정한다면 for문 반복하며
  length에 도달하기 전까지는 9 * (10^(i-1)) * i 를 누적 합
  length에 도달하면 (a-10^(i-1)+1) * i

2.시간 복잡도
- 시간 제한: 0.15초
- O()
"""
import sys
input = sys.stdin.readline

N = input().rstrip()
length = len(N)-1
res = 0

# 자릿수 기반으로 개수 구하기
for i in range(length):
    res += 9*(10**i)*(i+1)
    
# 자릿수를 제외한 나머지 숫자 구하기
res += ((int(N) - (10**length))+1) * (length+1)

print(res)
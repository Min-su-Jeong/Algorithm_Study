"""
1. 전략
- 브루트포스(Brute Force)
- 아홉 난쟁이의 키 list에서 2개씩 제외한 나머지의 합 = 100인 것 구하기

2. 시간복잡도
- O(1) = 9^2 = 81
"""
# Input
height = [int(input()) for _ in range(9)]

# Solution
idx1, idx2 = -1, -1
for i in range(9):
    for j in range(i+1, 9):

        # 키가 100인 경우 찾기
        if sum(height) - (height[i] + height[j]) == 100:
            idx1 = height[i]
            idx2 = height[j]
            
height.remove(idx1)
height.remove(idx2)
height.sort()

# Output
for i in range(7):
    print(height[i])
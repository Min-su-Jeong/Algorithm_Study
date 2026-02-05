N = int(input())
S = list(map(int, input().split()))

ret = 0
left = 0
fruit = {}

for right in range(N):
    if S[right] not in fruit:
        fruit[S[right]] = 0
    fruit[S[right]] += 1
    
    while len(fruit) > 2:
        fruit[S[left]] -= 1
        if fruit[S[left]] == 0:
            del fruit[S[left]]
        left += 1
    
    ret = max(ret, right - left + 1)

print(ret)
n = int(input())

# n의 방법의 수: n-2 + n-1
# n-2 -> 누워있는 두개의 타일이 붙고, n-1 -> 세워져 있는 한개의 타일이 붙음
s = [0, 1, 2]
for i in range(3, 1001):
    s.append(s[i - 2] + s[i - 1])
    
print(s[n] % 10007)
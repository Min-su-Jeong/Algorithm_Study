import sys
input = sys.stdin.readline

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a

n = int(input().strip())
arr = list(map(int, input().split()))

i = arr[0]
ret = 0
for x in arr[1:]:
    ret = gcd(ret, x - i)

print(abs(ret))
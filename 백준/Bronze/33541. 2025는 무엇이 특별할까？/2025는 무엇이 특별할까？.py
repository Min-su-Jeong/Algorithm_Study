X = int(input())

MAX = 10000

def calc(a, b, x):
    ret = (a + b) ** 2
    if ret == x:
        return True
    else:
        return False
    
for i in range(X+1, MAX):
    a = i // 100
    b = i % 100

    ret = calc(a, b, i)

    if ret:
        print(i)
        exit(0)

print(-1)
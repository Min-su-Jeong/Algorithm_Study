import sys

def div(x, y, n):
    global w, b
    c = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if c != paper[i][j]:
                div(x, y, n//2)
                div(x, y+n//2, n//2)
                div(x+n//2, y, n//2)
                div(x+n//2, y+n//2, n//2)
                return
    if c == 0:
        w += 1
    else:
        b += 1

input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0

div(0, 0, n)
print(w, b, sep='\n')
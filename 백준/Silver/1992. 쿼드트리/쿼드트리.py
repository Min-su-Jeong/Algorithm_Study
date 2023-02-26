import sys

def quadTree(x, y, n):
    check = img[x][y]   
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != img[i][j]:
                print('(', end='')
                quadTree(x, y, n//2)
                quadTree(x, y+n//2, n//2)
                quadTree(x+n//2, y, n//2)
                quadTree(x+n//2, y+n//2, n//2)
                print(')', end='')
                return
    print(check, end='')

input = sys.stdin.readline
n = int(input())
img = [input().rstrip() for _ in range(n)]
quadTree(0, 0, n)
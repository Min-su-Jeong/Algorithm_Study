import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

def quad(y, x, size):
    if size == 1:
        return str(img[y][x])
    
    check = img[y][x]
    ret = ""

    for i in range(y, y+size):
        for j in range(x, x+size):
            if check != img[i][j]:
                ret += '('
                ret += quad(y, x, size//2)
                ret += quad(y, x+size//2, size//2)
                ret += quad(y+size//2, x, size//2)
                ret += quad(y+size//2, x+size//2 , size//2)
                ret += ')'
                return ret
    
    return str(img[y][x])

if __name__ == "__main__":
    N = int(input())
    img = [list(map(int, input())) for _ in range(N)]
    
    print(quad(0, 0, N))
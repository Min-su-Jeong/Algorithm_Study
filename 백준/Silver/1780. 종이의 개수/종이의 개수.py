import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
neg, neu, pos = 0, 0, 0

def clip_paper(x, y, n):
    global neg, neu, pos
    num_check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if(paper[i][j] != num_check):
                for k in range(3):
                    for l in range(3):
                        clip_paper(x + k * n//3, y + l * n//3, n//3)
                return
            
    if(num_check == -1):
        neg += 1
    elif(num_check == 0):
        neu += 1
    else:
        pos += 1
        
clip_paper(0, 0, n)
print(f'{neg}\n{neu}\n{pos}')
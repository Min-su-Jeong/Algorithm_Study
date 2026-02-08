H, W = map(int, input().split())
graph = [list(map(str, input())) for _ in range(H)]
sky = [[-1] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if graph[i][j] == 'c':
            sky[i][j] = 0

for i in range(H):
    for j in range(W):
        if sky[i][j] != 0:
            continue

        while j+1 < W and sky[i][j+1] == -1:
            sky[i][j+1] = sky[i][j] + 1
            j += 1

for i in range(H):
    for j in range(W):
        print(sky[i][j], end=' ')
    print()
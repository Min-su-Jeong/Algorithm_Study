def dfs(depth: int, dwarfIdx: int):
    if depth == 7:
        if sum(sevenDwarves) == 100:
            for i in sorted(sevenDwarves):
                print(i)
            exit()
        else:
            return
        
    for i in range(dwarfIdx, len(dwarves)):
        sevenDwarves.append(dwarves[i])
        dfs(depth+1, i+1)
        sevenDwarves.pop()

dwarves = [int(input()) for _ in range(9)]
sevenDwarves = []
dfs(0, 0)
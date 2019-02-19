def cavityMap(grid):
    lenGrid = len(grid)
    spacePresent = False
    if grid[0].find(" ") != -1:
        spacePresent = True
    for i in range(lenGrid):
        if spacePresent:
            grid[i] = list(map(int,grid[i].split(" ")))
        else:
            grid[i] = list(map(int,list(grid[i])))
    for i in range(1,lenGrid-1):
        for j in range(1,lenGrid-1):
            if grid[i][j] > int(grid[i-1][j]) and grid[i][j] > int(grid[i+1][j]) \
            and grid[i][j] > int(grid[i][j-1]) and grid[i][j] > int(grid[i][j+1]):
                grid[i][j] = 101
    for i in range(lenGrid):
        if spacePresent:
            grid[i] = ' '.join(list(map(str,grid[i])))
        else:
            grid[i] = ''.join(list(map(str,grid[i])))
        grid[i] = grid[i].replace("101","X")
    return grid
arr = ["63456754","68335522","25482912",
"54429472",
"35416147",
"75848666",
"41633675",
"82511989"]
print(cavityMap(arr))
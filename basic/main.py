def display_grid(grid):
    print(grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
    print("---+---+---")
    print(grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
    print("---+---+---")
    print(grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])


def Win(grid):
    if grid[0][0] == grid[0][1] == grid[0][2] and grid[0][0] != "":
        return grid[0][0]
    if grid[1][0] == grid[1][1] == grid[1][2] and grid[1][0] != "":
        return grid[1][0]
    if grid[2][0] == grid[2][1] == grid[2][2] and grid[2][0] != "":
        return grid[2][0]

    if grid[0][0] == grid[1][0] == grid[2][0] and grid[0][0] != "":
        return grid[0][0]
    if grid[0][1] == grid[1][1] == grid[2][1] and grid[0][1] != "":
        return grid[0][1]
    if grid[0][2] == grid[1][2] == grid[2][2] and grid[0][2] != "":
        return grid[0][2]

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "":
        return grid[0][2]

    for row in grid:
        if "" in row:
            return None

    return "Tie"
# i used ai for the row in grid part, i didnt know how to do tie
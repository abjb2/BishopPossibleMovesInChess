
def possible_bishop_positions(x, y):
    positions = []
    for i in range(1, 8):
        if x+i <= 7 and y+i <= 7:
            positions.append((x+i, y+i))
        if x-i >= 0 and y-i >= 0:
            positions.append((x-i, y-i))
        if x+i <= 7 and y-i >= 0:
            positions.append((x+i, y-i))
        if x-i >= 0 and y+i <= 7:
            positions.append((x-i, y+i))
    return positions


moves = possible_bishop_positions(4,4)
print(moves[0:3])


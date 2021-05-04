def get_field():
    field = [[1 for _ in range(50)] for _ in range(20)]
    for i in range(1, 49):
        for j in range(1, 19):
            field[j][i] = 2
    field[3][3] = 6
    field[16][47] = 0
    for y in range(6, 13):
        for x in range(10, 22):
            field[y][x] = 4
    return field

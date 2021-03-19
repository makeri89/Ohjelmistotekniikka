def get_field():
    field = [[1 for _ in range(50)] for _ in range(20)]
    for i in range(1, 49):
        for j in range(1, 19):
            field[j][i] = 2
    field[16][47] = 0
    for i in range(1, 10):
        field[i+4][26] = 1
        for j in range(42, 49):
            field[i][j] = 3
    field[6][10] = 6
    return field

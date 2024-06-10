
mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1

rows = len(mat)
cols = len(mat[0])

result = [[0] * cols for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        row_start = max(0, row - k)
        row_end = min(rows - 1, row + k)
        col_start = max(0, col - k)
        col_end = min(cols - 1, col + k)

        total = 0
        for r in range(row_start, row_end + 1):
            for c in range(col_start, col_end + 1):
                total += mat[r][c]
        
        result[row][col] = total


print(result)
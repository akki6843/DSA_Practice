import numpy as np


def get_kernalsum(r,c):
    
    return 100

mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
kernal = [[0]]
kernal = np.pad(kernal,k)
mat = np.pad(mat, k)
out = np.zeros_like(mat)

rows = mat.shape[0]
cols = mat.shape[1]
# print(rows, cols)

for r in range(k,rows-k):
    for c in range(k,cols-k):
        out[r][c] = get_kernalsum(r,c)


print(out)
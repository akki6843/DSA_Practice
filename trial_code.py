# nums = [0,1,1,3]
# # maximumBit = 2

# nums = [2,3,4,7]
# maximumBit = 3

# pre_xored = [0] * len(nums)
# pre_xored[0] = nums[0]
# k = 2**maximumBit
# out = []

# for i in range(1, len(nums)):
#     pre_xored[i] = pre_xored[i-1] ^ nums[i]

# for i in range(len(pre_xored), 0, -1):
#     print(i)
#     out.append((k-1)^pre_xored[i-1])


# print(out)


grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]

print(len(grid))

pool_window = [row[j:j+n] for row in grid[i:i+n]]
max_value = max([max(row) for row in pool_window])

output_matrix[i][j] = max_value




def max_pooling(input_matrix, pool_size=(2, 2), strides=(2, 2)):
    """
    Perform max pooling on the input matrix.

    Args:
    input_matrix: 2D input matrix (list of lists).
    pool_size: Tuple of 2 integers representing the size of the pooling window (height, width).
    strides: Tuple of 2 integers representing the strides (vertical, horizontal).

    Returns:
    output_matrix: 2D matrix after max pooling.
    """
    input_height, input_width = len(input_matrix), len(input_matrix[0])
    pool_height, pool_width = pool_size
    stride_vertical, stride_horizontal = strides

    # Calculate output dimensions
    output_height = (input_height - pool_height) // stride_vertical + 1
    output_width = (input_width - pool_width) // stride_horizontal + 1

    # Initialize output matrix
    output_matrix = [[0] * output_width for _ in range(output_height)]

    # Perform max pooling
    for i in range(0, input_height - pool_height + 1, stride_vertical):
        for j in range(0, input_width - pool_width + 1, stride_horizontal):
            # Get the pooling window
            pool_window = [row[j:j+pool_width] for row in input_matrix[i:i+pool_height]]
            # Find maximum value in the window
            max_value = max([max(row) for row in pool_window])
            # Assign maximum value to the output matrix
            output_matrix[i//stride_vertical][j//stride_horizontal] = max_value

    return output_matrix

# Example usage
input_matrix = [
    [1, 2, 1, 2],
    [2, 4, 3, 1],
    [1, 2, 2, 4],
    [2, 1, 2, 0]
]

pool_size = (2, 2)
strides = (2, 2)

output_matrix = max_pooling(input_matrix, pool_size, strides)
print("Input Matrix:")
for row in input_matrix:
    print(row)
print("\nOutput Matrix after Max Pooling:")
for row in output_matrix:
    print(row)

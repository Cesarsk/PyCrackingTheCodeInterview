"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?
"""


def rotate_matrix_pythonic_zip(matrix):
    """rotates a matrix 90 degrees clockwise"""
    # zip(*matrix) reads "by column" so [(1,4,7),(2,5,8),(3,6,9)]
    # if matrix is [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return [list(reversed(row)) for row in zip(*matrix)]


# todo study
def rotate_matrix(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    # row
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        # column
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

            # top -> right
            matrix[i][-layer - 1] = top
    return matrix


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

res = rotate_matrix(matrix)
print("result", res)

print(list(zip(*matrix)))

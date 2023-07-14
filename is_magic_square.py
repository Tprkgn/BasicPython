def is_magic_square(matrix):
    # Check if the matrix is square
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    # Get the size of the matrix
    size = len(matrix)

    # Get the sum of the first row
    target_sum = sum(matrix[0])

    # Check the sums of the rows
    for row in matrix:
        if sum(row) != target_sum:
            return False

    # Check the sums of the columns
    for i in range(size):
        column_sum = 0
        for row in matrix:
            column_sum += row[i]
        if column_sum != target_sum:
            return False

    # Check the sum of the diagonal from top left to bottom right
    diagonal_sum = 0
    for i in range(size):
        diagonal_sum += matrix[i][i]
    if diagonal_sum != target_sum:
        return False

    # Check the sum of the diagonal from top right to bottom left
    diagonal_sum = 0
    for i in range(size):
        diagonal_sum += matrix[i][size - i - 1]
    if diagonal_sum != target_sum:
        return False

    # If all sums are equal to the target sum, return True
    return True

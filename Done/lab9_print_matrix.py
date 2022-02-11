def print_matrix(matrix):
    for i in range(len(matrix)):
        print("".join("{:^15g}".format(matrix[i][j]) for j in range(len(matrix[0]))))

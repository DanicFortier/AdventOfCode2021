# Tests are made here with the smaller dataset
def init_matrix(size):
    matrix = []

    for i in range(size[1] + 1):
        matrix.append([0] * (size[0] + 1))

    return matrix

if __name__ == "__main__":
   x = 10
   y = 3
   matrix = init_matrix((x, y))
   print(matrix)


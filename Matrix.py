class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        #the matrix attribute of the class
        self.matrix = matrix = []

        # initialize the size of matrix
        for i in range(rows):
            row = [0] * columns
            matrix.append(row)

        # assign values to the identity
        for i in range(rows):
            for j in range(columns):
                if i == j:
                    matrix[i][j] = 1

    def __str__(self):
        #string representation of the matrix
        string = ""
        for i in range(self.rows):
            string += str(self.matrix[i])
            string += "\n"

        return string



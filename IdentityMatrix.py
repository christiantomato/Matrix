from Matrix import *

class IdentityMatrix(Matrix):

    #define a new constructor, all we need is size of identity
    def __init__(self, size):
        #dimension of the identity matrix
        self.size = size

        #size is equal to rows and columns
        self.rows = self.columns = self.size

        # the 2D array, or matrix, attribute of the class
        self.matrix = matrix = []

        # initialize the size of matrix
        for i in range(self.size):
            row = [0] * self.size
            matrix.append(row)

        #assign values to make it an identity
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    matrix[i][j] = 1





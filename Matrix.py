import math

class Matrix:

    #the parameters to pass in for a matrix
    def __init__(self, num_rows, num_columns, entries):
        self.rows = num_rows
        self.columns = num_columns
        #where entries is a list of the entries read from row to row
        self.entries = entries
        #size for easy size comparisons and stuff (in form m x n)
        self.size = [self.rows, self.columns]
        #boolean describing whether matrix is square or not
        self.square = (self.rows == self.columns)
        #define dimension if square
        if self.square:
            self.dimension = self.rows

        #the 2D array, or matrix, attribute of the class
        self.matrix = matrix = []

        #initialize the size of matrix
        for i in range(self.rows):
            row = [0] * self.columns
            matrix.append(row)

        #index variable for the entries array we passed in
        entry = 0
        # add the entries to matrix
        for i in range(self.rows):
            for j in range(self.columns):
                matrix[i][j] = entries[entry]
                entry += 1

    #string representation of matrix
    def __str__(self):
        string = "\n"
        for i in range(self.rows):
            string += str(self.matrix[i])
            string += "\n"

        return string

    #defining equality between two matrices
    def __eq__(self, other):
        #check to make sure other is actually a matrix object
        if isinstance(other, Matrix):
            #check equality of each 2D array
            return self.matrix == other.matrix
        else:
            #raise an exception
            raise TypeError(other + "is not a Matrix")

    #define matrix addition
    def __add__(self, other):
        #can only add together if they are both matrices
        if isinstance(other, Matrix):
            #check if they are both the same size
            if self.size == other.size:
                #then they are the same size, create new matrix with added entries
                added_entries = []
                #loop through all the entries and add them to other
                for i in range(len(self.entries)):
                    #add the entries
                    added_entries.append(self.entries[i] + other.entries[i])
                #return the new matrix
                sum_matrix = Matrix(self.rows, self.columns, added_entries)
                return sum_matrix
            else:
                #raise an exception
                raise TypeError("Matrices are not the same size")
        else:
            #raise an exception
            raise TypeError(other + "is not a Matrix")

    #define matrix subtraction
    def __sub__(self, other):
        #can only add together if they are both matrices
        if isinstance(other, Matrix):
            #check if they are both the same size
            if self.size == other.size:
                #then they are the same size, create new matrix with subtracted entries
                subtracted_entries = []
                #loop through all the entries and subtract them from self
                for i in range(len(self.entries)):
                    #subtract the entries
                    subtracted_entries.append(self.entries[i] - other.entries[i])
                #return the new matrix
                sub_matrix = Matrix(self.rows, self.columns, subtracted_entries)
                return sub_matrix
            else:
                #raise an exception
                raise TypeError("Matrices are not the same size")
        else:
            #raise an exception
            raise TypeError(other + "is not a Matrix")

    #define matrix multiplication
    def __mul__(self, other):
        #check other is a matrix object
        if isinstance(other, Matrix):
            #check if they can be multiplied (m x n * n x r = m x r)
            if self.columns == other.rows:
                #compute the dot product with each row and column, each ij entry of the new matrix is a dot product
                multiplied_entries = []
                dot_product = 0

                #loop that will change between the left matrix row
                for m in range(self.rows):
                    #loop that will go through the right matrix columns
                    for r in range(other.columns):
                        #for loop that dots each corresponding entry
                        for n in range(self.columns):
                            #compute the dot
                            dot_product += self.matrix[m][n] * other.matrix[n][r]

                        #add the dot product to the entry array
                        multiplied_entries.append(dot_product)
                        #restart the dot product here before next dot iteration
                        dot_product = 0

                #finally, return the new matrix
                mul_matrix = Matrix(self.rows, other.columns, multiplied_entries)
                return mul_matrix

    #define matrix powers
    def __pow__(self, power, modulo=None):
        #do a delayed import to get the identity
        from IdentityMatrix import IdentityMatrix

        #matrix powers only defined for square matrices
        if self.square:
            #compute the power, start with identity for corresponding size
            result = IdentityMatrix(self.dimension)
            for i in range(power):
                result = result * self

            return result

    #algorithm that row reduces the matrix
    def row_reduce(self):

        """
        Example Matrix:

        1 2 3
        3 7 7
        2 5 9

        1. clear out under first column
        2. go through next row, locate entry that is directly below row
        3. scalar multiply each one by each other to yield same number
        4. negate the bottom row and add it to the top row
        5. repeat for subsequent rows that are below the current row
        6. repeat the same process but this time use the next row to clear out below it.
        """

        #locate

    #function to check if row reduced
    def is_row_reduced(self):
        #boolean variables for different row reduced forms - start as true, change if found false
        reduced_form = True
        echelon_form = True

        #sentinel value as -1 to start, since we are checking if the leading entry is less than current column number
        leading_entry_index = -1

        #find the leading entry position of each row and compare it to leading entry of the next row
        for i in range(self.rows):
            for j in range(self.columns):
                #if it is a nonzero entry
                if self.matrix[i][j] != 0:
                    #if the nonzero entry is further right than previous nonzero entry
                    if j > leading_entry_index:
                        #meets row reduced requirements, set the leading entry
                        leading_entry_index = j
                        #check for zeroes up above leading entry
                        #start at previous row, go back up each row at a time, make sure not to go past row index 0.
                        for x in range(i-1, -1, -1):
                            #if any of the above entries are not zero
                            if self.matrix[x][j] != 0:
                                #not meeting row echelon requirements
                                echelon_form = False
                        #move onto next row if everything is successful
                        break
                    else:
                        #not row reduced (so not echelon either), then we can finish
                        reduced_form = False
                        echelon_form = False
                        return "Row Reduced Form: %s, Row Echelon Form: %s" % (reduced_form, echelon_form)

        #return the form that it is in
        return "row reduced: %s, echelon form: %s" % (reduced_form, echelon_form)

    #function to simplify a row
    def simplify(self, row):
        # subtract 1 from the desired row since arrays start at 0
        row -= 1

        all_entries = []

        for j in range(self.columns):
            all_entries.append(self.matrix[row][j])

        gcd = math.gcd(*all_entries)

        #simplify if possible
        if gcd > 1:
            for j in range(self.columns):
                self.matrix[row][j] = int(self.matrix[row][j]/gcd)

    #functions for elementary row operations below!

    def scale_row(self, row, scalar):
        #subtract 1 from the desired row since arrays start at 0
        row -= 1

        #multiply each entry by the scalar
        for j in range(self.columns):
            #let's deal with just integers for now
            self.matrix[row][j] = int(self.matrix[row][j] * scalar)

    # add rows - the manipulated row is the one that gets changed
    def add_rows(self, manipulated_row, row_added):
        #subtract 1 from desired rows since arrays start at 0
        manipulated_row -= 1
        row_added -= 1

        #update manipulated row by adding all entries
        for j in range(self.columns):
            self.matrix[manipulated_row][j] += self.matrix[row_added][j]

    #function that implements the elementary operations more effectively for faster linear combinations
    def scale_add_rows(self, scalar1, row1, scalar2, row2):
        #scale and add
        self.scale_row(row1, scalar1)
        self.scale_row(row2, scalar2)
        self.add_rows(row1, row2)
        # scale back the row that wasn't changed by multiplying by inverse
        self.scale_row(row2, (1/scalar2))
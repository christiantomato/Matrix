class Matrix:

    #the parameters to pass in for custom matrix
    def __init__(self, rows, columns, entries):
        self.rows = rows
        self.columns = columns
        self.entries = entries

        #the 2D array, or matrix, attribute of the class
        self.matrix = matrix = []

        # initialize the size of matrix
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

    #method to check if row reduced
    def is_row_reduced(self):
        #sentinel value as -1 to start, since we are checking if the leading entry is less than current column number
        leading_entry_index = -1

        #check for leading entry position of each row and compare it to next
        for i in range(self.rows):
            for j in range(self.columns):
                #if it is a nonzero entry
                if self.matrix[i][j] != 0:
                    #if the nonzero entry is further right than previous nonzero entry
                    if j > leading_entry_index:
                        #meeting row reduced requirements, set new leading entry, go to next row
                        leading_entry_index = j
                        break
                    else:
                        #not row reduced, finish function
                        return False

        #return true if it is found that it isn't false
        return True


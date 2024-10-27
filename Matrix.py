import math

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


    #algorithm that creates zeroes below a leading entry
    def row_reducing_algorithm(self, row_start):

        """
        1. take a row, locate first nonzero entry
        2. go through next row, locate entry that is directly below row
        3. scalar multiply each one by each other to yield same number
        4. negate the bottom row and add it to the top row
        5. repeat for subsequent rows that are below the current row
        6. repeat the same process but this time use the next row to clear out below it.
        """

        #variables:

        #start with negative so we can determine when an index has actually been found
        leading_entry_index = -1

        #don't allow a below entry index to start, once a leading entry is found it will be set
        below_entry_index = -1

        #keep track of both rows as well
        leading_entry_row = 0
        below_entry_row = 0

        #the actual entry values
        leading_entry = 0
        below_entry = 0

        #this important variable determines which row is being used to clear out everything below it
        row_clearer = row_start

        #locate the leading entry and compare to all rows below it
        while row_clearer < self.rows:
            for j in range(self.columns):

                #if it is a nonzero entry
                if self.matrix[row_clearer][j] != 0:
                    #if a leading entry has been set, now we search for below entry
                    if leading_entry_index >= 0:
                        # assign the below entry value, index, and row (row+1 since "i" is the index)
                        below_entry = self.matrix[row_clearer][j]
                        below_entry_index = j
                        below_entry_row = row_clearer + 1

                        # now check if they are actually in the same column
                        if leading_entry_index == below_entry_index:
                            # do row addition here to get zeros below
                            # remember to scale each row by the other rows entry, and negate a row to get 0
                            self.scale_add_rows(leading_entry, below_entry_row, -1*below_entry, leading_entry_row)
                            #simplify the rows after addition? (this is implemented in the functions already)

                        else:
                            # if not, then go to next row and check there
                            break

                    #if we haven't found an initial leading entry yet
                    elif below_entry_index < 0:
                        # assign the leading entry value, index, (and row+1 since "i" is the index)
                        leading_entry = self.matrix[row_clearer][j]
                        leading_entry_index = j
                        leading_entry_row = row_clearer + 1
                        # break, go to next row, and start looking for the entry directly below
                        break
            #increment to next row
            row_clearer += 1


    def row_reduce(self):
        #use the row reducing algorithm paired with the row reduce check to continue row reducing
        #do the algorithm for every row and it should reduce
        for i in range(self.rows):
            self.row_reducing_algorithm(i)
        #now simplify each row if possible
        for i in range(self.rows):
            #i + 1 because the function takes in actual row number and not index
            self.simplify(i+1)



    #function to check if row reduced
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
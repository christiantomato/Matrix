from IdentityMatrix import *

#function to get user input of a matrix
def make_matrix():

    print("Making new matrix.")

    #ask for dimensions of the matrix
    rows = int(input("rows of the matrix: "))
    columns = int(input("columns of the matrix: "))

    #row and col variables to aid in inputting entries
    row_num = 1
    col_num = 1
    matrix_entries = [0] * (rows * columns)
    #get all the entries for the matrix
    for i in range((rows * columns)):
        #update row_num and col_num once reached next row
        if i % columns == 0 and i != 0:
            row_num += 1
            col_num = 1

        #ask for the entries by row
        matrix_entries[i] = int(input("type in row %d entry %d: " % (row_num, col_num)))
        # increment column number
        col_num += 1

    #make and return the matrix
    custom_matrix = Matrix(rows, columns, matrix_entries)
    return custom_matrix

def main():

    my_matrix1 = make_matrix()


    print("matrix1: ", my_matrix1)

    print("power of 11: ", my_matrix1**11)

    #print(my_matrix.is_row_reduced())

    #my_matrix.row_reduce()
    #print("\nrow reduced: ", my_matrix)

    #print("\nyour identity matrix: ", my_identity_matrix)
    #print("row reduced for identity is always: ", my_identity_matrix.is_row_reduced())

#run
main()



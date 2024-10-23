from IdentityMatrix import *

#function to get user input of a matrix
def make_matrix():

    # ask for dimensions of the matrix
    rows = int(input("rows of the matrix: "))
    columns = int(input("columns of the matrix: "))

    row_num = 1
    col_num = 1
    matrix_entries = [0] * (rows * columns)
    for i in range((rows * columns)):
        # update row_num and col+_num once reached next row
        if i % columns == 0 and i != 0:
            row_num += 1
            col_num = 1

        # ask for the entries by row
        matrix_entries[i] = int(input("type in row %.d entry %.d: " % (row_num, col_num)))
        # increment column number
        col_num += 1

    custom_matrix = Matrix(rows, columns, matrix_entries)
    return custom_matrix

def main():

    my_matrix = make_matrix()
    my_identity_matrix = IdentityMatrix(5)
    print("\nyour matrix: ", my_matrix)
    print("is it row reduced?: ", my_matrix.is_row_reduced())
    print("\nyour identity matrix: ", my_identity_matrix)
    print("row reduced for identity is always: ", my_identity_matrix.is_row_reduced())

#run
main()



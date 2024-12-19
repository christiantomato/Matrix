from Matrix import *

class IdentityMatrix(Matrix):

    #define a new constructor, since all we need is the size of the identity matrix
    def __init__(self, size):

        #create the list of entries for the identity (one's down the diagonal)
        entries = []

        for i in range(size):
            for j in range(size):
                if i == j:
                    #if on a diagonal, assign 1's
                    entries.append(1)
                else:
                    #assign 0's
                    entries.append(0)

        #finally, call to super
        #note rows and columns are same length
        super().__init__(size, size, entries)


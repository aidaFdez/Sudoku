import numpy
import random

visited = [] #Array of the visited states
queue = [] #Array with the queue of states to visit, will be used as a stack.
#sudoku = numpy.zeros(81)

def checkPossible (position, number, sudo):
    numB = position % 9
    i = 0
    j = numB

    #Checks that number does not happen in the same column.
    while j < position:
        if number == sudo[j]:
            return False
        j = j+9
    k = int(position/9)*9 #Sets the beginning of the row in k
    l = k+9 #Sets the ending of the row in l

    #Checks that the number does not happen in the row.
    while (k< position):
        if number == sudo[k]:
            return False
        k = k+1

    k = int(position/27)*27 #Sets the beginning of the first square of the row of squares
    k = k + (int(numB/3)*3) #Sets the beginning of the square

    #Checks the number does not happen in the same square.
    j = 0
    while ((k< position) and (j < 3)):
        b = k
        l = 0
        while l<3:
            if number == sudo [b]:
                return False
            b = b+1
            l = l+1
        k = k+9
        j = j+1
    return True

#array.insert(index, value)
def createSudo (visit, que):
    if (len (que[0]) == 81) and not (que[0][80]==0):
        return que[0]

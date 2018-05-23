import numpy
import random

visited = [] #Array of the visited states
queue = [[]] #Array with the queue of states to visit, will be used as a stack.
#sudoku = numpy.zeros(81)

def checkPossible (position, number, sudo):
    numB = position % 9
    i = 0
    j = numB
    sudo = sudo + [0]

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
    b = 0
    while ((k< position) and (j < 3) and (b<position)):
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

def addOne(number):
    if number == 9:
        return 1
    return (number +1)

#List of the possible next states given another
def nextOnes(num, sudo, visit):
    l = 0
    toRet = []
    while l<9:
        #print (l)
        #print (checkPossible(len(sudo),num, sudo + [0]))
        if checkPossible(len(sudo),num, sudo + [0]):
            #Do not add if it has been visited
            if not (sudo + [num]) in visit:
                toRet.append(sudo + [num])
        num = addOne(num)
        l = l+1
    return toRet

#def createSudo (visit, que):
    #If the sudoku is completed, then return it
#    if (len (que[0]) == 81): #and not (que[0][80]==0):
#        return que[0]
    #If the sudoku is not completed, keep completing it
#    if not (que[0] in visit):
#        a = random.randint(1,9)
#        possibles = nextOnes(a, que[0])
        #If the sudoku is not possible to complete from that state,the length of possibles is 0
#        if len(possibles) == 0:
#            return createSudo (visit, que[1:])
#        else:
#            que = possibles + que
#            return createSudo (visit, que)
#    return createSudo(visit, que[1:])

def createSudo (visit, que):
    l = 0
    #while not (len(que[0]) == 81):
    while not (len(que[0]) == 81):
        #print(que)
        if que[0] in visit:
            que = que[1:]
        else:
            visit = visit + [que[0]]
            a = random.randint(1,9)
            possibles = nextOnes(a,que[0], visit)
            if len(possibles) == 0:
                que = que[1:]
            else:
                que = possibles + que
        #print (len(que[0]))
        #print(" \n")
        #l = l+1
        #print(visit)
    return que[0]

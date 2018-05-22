visited = []
queue = []

def checkPossible (position, number, sudo):
    numB = number % 9
    i = 0
    j = numB

    #Checks that number does not happen in the same column.
    while j < 81:
        if number == sudo(j):
            return False
        j = j+9
    k = int(number/9)*9 #Sets the beginning of the row in k
    l = k+9 #Sets the ending of the row in l

    #Checks that the number does not happen in the row.
    while k< l:
        if number == sudo[k]:
            return False
        k = k+1
    k = int(number/3)*3 #Sets the beginning of the square

    #Checks the number does not happen in the same square.
    while k<81:
        b = k
        l = 0
        while l<3:
            if number == sudo (b):
                return False
            b = b+1
        k = k+9

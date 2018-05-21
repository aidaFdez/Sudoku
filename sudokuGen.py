visited = []
queue = []

def checkPossible (position, number, sudo):
    numB = number % 9
    i = 0
    j = numB
    #Checks that number does not happen in the same column
    for j<81:
        if number == sudo(j):
            return False
        j = j+9
    k = int(number/9)*9 #Sets the beginning of the row in k
    l = k+9 #Sets the ending of the row in l
    for k< l:
        if number = sudo[k]:
            return False
        k++

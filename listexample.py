import random 


def getrandomlist():
    L = [random.randint(1,6) for i in range(10)]
    return L


L = getrandomlist()
def ibubblesort(L):
    swapped = True
    while swapped:
        swapped = False
    for position in range (len(L) - 1):
         if L[position] > L[position+1]:
            L[position], L[position+1] = L[position+1], L[position]
            swapped = True

    return L
   


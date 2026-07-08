#print numbers n to 1
def printNumbers(n):

    if n == 0:
        return

    print(n)

    printNumbers(n-1)
#print numbers n to 1
def printNumbers(n):

    if n == 0:
        return

    print(n)

    printNumbers(n-1)
    
  
#factorial of a number
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)


#sum of n numbers
def sumN(n):

    if n == 0:
        return 0

    return n + sumN(n-1)    

    
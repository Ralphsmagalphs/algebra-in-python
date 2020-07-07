import functools
import operator

#Determines if a specific set of values for an operation commutes.
#Commutatifity means that switching the values will not affect the end result.
def isCommutative(function, a,b):
    return (function(a,b) == function(b,a))

#Determines if a specific set of values for an operation associates
#Associativity means that, for an operation *, a*(b*c) = (a*b)*c
def isAssociative(function, a, b, c):
    return (function(function(a,b), c) == function(a, function(b,c)))

def displayCommutativity(operatorName, operatorFunc, A, B):
    print( f"{operatorName} with ({A}, {B}) is ", end = '')
    if not isCommutative(operatorFunc, A, B):
        print("not ", end='')
    print("commutative")


def displayAssociativity(operatorName, operatorFunc, A, B, C):
    print(f"{operatorName} with ({A}, {B}, {C}) is ", end='')
    if not isAssociative(operatorFunc, A, B, C):
        print("not ", end = '')
    print("associative")



def main():

    adding = functools.partial(operator.add)
    subtract = functools.partial(operator.sub)

    displayCommutativity("subtraction", subtract, 3, 5)
    displayAssociativity("subtraction", subtract, 6, 6, 3)


if __name__ == "__main__":
    main()

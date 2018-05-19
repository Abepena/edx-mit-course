"""
The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

 Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.
"""


# def gcdIter(a, b):
#     '''
#     a, b: positive integers

#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     # Your code here
#     if  a < b:
#        result = a
#     else:
#         result = b

#     while result > 1:
#         if a % result == 0 and b % result == 0:
#             break
#         else:
#             result -=1

#     return result

# print(gcdIter(17,12))


#######ANSWER


def gcd(a, b):
    """
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    """
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue


# RECURSION
# The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

# gcd(2, 12) = 2

# gcd(6, 12) = 6

# gcd(9, 12) = 3

# gcd(17, 12) = 1

# A clever mathematical trick(due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

# If b = 0, then the answer is a

# Otherwise, gcd(a, b) is the same as gcd(b, a % b)


def gcd_recur(a, b):

    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)


print(gcd_recur(6, 12))

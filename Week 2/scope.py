# Functions as arguments
# -arguments can take on any type, even functions


def func_a():
    print("Inside of func_a")


def func_b(y):
    print("Inside of func_b")
    return y


def func_c(z):
    print("Inside of func_c")
    return z()


print(func_a())
print(5 + func_b(2))
print(func_c(func_a))


print()
print()

# Function inside a function


def g(x):

    def h():
        x = "abc"

    x = x + 1
    print("in g(x): x =", x)
    h()
    return x


x = 3
z = g(x)
"""
Should return print statement with x = x+1
then return x+1 to z
"""

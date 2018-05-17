# Example of a square root using Bisection Search
# Attempting to find the square root of x

x=25
epsilon = 0.01
numGuesses = 0
low = 1
high = x
ans = (high + low) / 2

while abs(ans**2 -x) >= epsilon:
    print ('low = ' + str(low) + ' high = ' + str(high) + " ans = " + str(ans))
    numGuesses += 1

    if ans**2 < x:
        low = ans
    else:
        high = ans

    ans = (high + low) / 2

print ("Number of guesses: " + str(numGuesses))
print (str(ans)+ " is close to the square root of " + str(x) )

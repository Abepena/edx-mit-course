"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
Lowest Payment: 180 

Assume that the interest is compounded monthly according to the balance at the end of the month(after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay.


	      Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310
      
"""

## functions
def check_minimum(balance, payment):
    """
    Input: balance and minimum payment guess
    Output: boolean representing if the minimum payment will pay off the balance in a year
    """
    for month in range(12):
        unpaid = balance - payment
        balance = unpaid + unpaid * annualInterestRate / 12

    return balance < 0


### Main

# initialize variables
payment = 10
balance = 4773
annualInterestRate = 0.2

#loop and increment until payment is enough
while check_minimum(balance, payment) == False:
    payment += 10

print("Lowest payment: {}".format(payment))

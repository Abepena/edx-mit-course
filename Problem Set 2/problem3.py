"""
 You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount(in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

 Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!



 Test Case 1:
"""
balance = 320000
annualInterestRate = 0.2

unpaid_balance = 0
monthly_interest_rate = annualInterestRate / 12
low_bal = balance / 12
high_bal = (balance * (1 + monthly_interest_rate) ** 12) / 12
min_monthly_payment = (low_bal + high_bal) / 2

while True:
    rem_balance = balance
    for i in range(12):
        unpaid_balance = rem_balance - min_monthly_payment
        rem_balance = unpaid_balance + unpaid_balance * monthly_interest_rate

    if abs(rem_balance) <= .01:
        break
    else:
        if rem_balance > 0:
            low_bal = min_monthly_payment
        else:
            high_bal = min_monthly_payment

    min_monthly_payment = (low_bal + high_bal) / 2

print("Lowest Payment: {}".format(round(min_monthly_payment, 2)))

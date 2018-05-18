# In this problem, you'll create a program that guesses a secret number!
#
# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

# ** Your program should use bisection search. So think carefully what that means. What will the first guess always be? How should you calculate subsequent guesses?
#
# ** Your initial endpoints should be 0 and 100. Do not optimize your subsequent endpoints by making them be the halfway point plus or minus 1. Rather, just make them be the halfway point.

# Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.
#
# When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then, you should re-ask the question, and prompt again for input. For example:

##USER PROMPT FUNCTION loops until they type h l or c
def get_choice():

    while True:
        print("Is your secret number {}".format(ans))
        choice = input(
            "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
        ).lower()

        if choice == "h" or choice == "l" or choice == "c":
            break
        else:
            print("Sorry, I did not understand your input.")
    return choice


##MAIN CODE
low = 0
high = 100
ans = int((high + low) / 2)
choices = ["h", "l", "c"]


print("Please think of a number between 0 and 100")
while True:
    choice = get_choice()
    if choice == "h":
        high = ans
    elif choice == "l":
        low = ans
    elif choice == "c":
        break
    ans = int((high + low) / 2)

print("Game over. Your secret number was: {}".format(ans))

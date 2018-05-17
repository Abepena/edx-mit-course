# Problem 2
# 0.0/10.0 points (graded)
# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#


def bob_count(s):
    count = 0

    for index, letter in enumerate(s[:-2]):
        if "".join(s[index:index + 3]) == "bob":
            count += 1
    print(f"Number of times bob occurs is: {count}")


bob_count('gbobobetbob')

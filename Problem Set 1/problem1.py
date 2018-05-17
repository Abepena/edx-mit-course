# Problem 1
# 10/10 points (graded)
# Assume s is a string of lower case characters.
#
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

def count_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1

    print("Number of vowels: {}".format(count))


count_vowels("azcbobobegghakl")

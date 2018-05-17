# Problem 3
# 0.0/15.0 points (graded)
# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
import string


def longest_substring(s):

    lowercase = string.ascii_lowercase
    count = 0
    substring = ""
    longest = ""

    for i, letter in enumerate(s):
        substring += letter

        if len(substring) > len(longest):
            longest = substring

        if i != len(s)-1 and lowercase.index(letter) <= lowercase.index(s[i + 1]):
            continue
        elif i == len(s)-1 and lowercase.index(letter) >= lowercase.index(s[i - 1]):
            if len(substring) > len(longest):
                longest = substring
        else:
            substring = ""

    print("Longest substring in alphabetical order is: {}".format(longest))


longest_substring(s="asdhkasjhdgadsyugdygdavsdayugasdh")

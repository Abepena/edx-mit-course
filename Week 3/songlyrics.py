"""
Stripping punctuation
https://stackoverflow.com/questions/34293875/how-to-remove-punctuation-marks-from-a-string-in-python-3-x-using-translate
"""

import string, sys, pyperclip

def strip_punctuation(s):
    """
    Assumes s is a string with punctuation
    Returns string without punctuation
    """
    translator = s.maketrans("", "", string.punctuation)
    return s.translate(translator)


def lyric_list(lyrics):
    """
    Input: string of lyrics
    Output: returns list every word in lyrics split by spaces
    """
    return strip_punctuation(lyrics).strip().split(" ")


def lyrics_to_frequencies(lyrics):
    """
    assumes lyrics is a list of strings composing every
    word of a song 
    """
    my_dict = {}
    for word in lyrics:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict


print("Paste in the lyrics of your favorite song\nOnce pasted in press Enter then Ctrl+d on Linux/Mac or Ctrl-z on Windows: ")

#Allow the user to paste multiple lines of code in the shell
#Not necessary in Jupyter Notebook
# https: // stackoverflow.com/questions/34889012/how-to-paste-multiple-lines-of-text-into-python-input

lines = []

try:
    while True:
        lines.append(input())
except EOFError:
    pass

lyrics = lyric_list(" ".join(lines))
print(lyrics_to_frequencies(lyrics))

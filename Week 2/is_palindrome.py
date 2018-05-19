import string

def is_palindrome(s):
    """
    Defines a function that recursively checks if a 
    string input is a palindrome
    """

    def to_chars(s):
        """
        strips an input string of all punctuation and spaces
        """
        result = ''
        for c in s:
            s = s.lower()
            if c in string.ascii_lowercase:
                result += c
            return result

        
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    
    return is_pal(to_chars(s))

print(is_palindrome('Able was I, ere I saw Elba.'))

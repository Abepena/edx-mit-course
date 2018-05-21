#RECURSIVE FIBBONACCI
numfibcalls = 0


def fib(n):
    global numfibcalls
    numfibcalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


print(f"Fibonacci of 13: {fib(13)}")
print(f"Number of calls: {numfibcalls}")

# RECURSIVE DICTIONARY FIBONACCI

numfibefcalls = 0


def fib_efficient(number, dictionary):
    global numfibefcalls
    numfibefcalls += 1
    if number in dictionary:
        return dictionary[number]
    else:
        ans = fib_efficient(number-1, dictionary) + \
            fib_efficient(number-2, dictionary)
        dictionary[number] = ans
        return ans


base_case_dict = {1: 1, 2: 2}

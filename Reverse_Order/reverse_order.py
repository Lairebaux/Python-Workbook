"""
Write a program that reads integers from the user and stores them in a list. Use 0 as
a sentinel value to mark the end of the input. Once all of the values have been read
your program should display them (except for the 0) in reverse order, with one value
appearing on each line.
"""

def reverse_order(s):
    user_input = s.split(" ")
    a = []
    for numbers in user_input:
        if numbers != "0":
            a.append(numbers)
    a.reverse()
    for numbers in a:
        print(numbers)

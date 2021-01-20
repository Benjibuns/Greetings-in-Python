# Challenge 1
# - Write a Python program to calculate the length of a string.
# - Extra credit:  Do it without a built in function.

string = "This is a string that i am using as a subject to make a program that will tell me the length of a string"

# len(string)

counter = 0

for _ in string:
    counter += 1

print(counter)

# Challenge 2
# - Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return an empty string.

short_string = "Benjamin"


def start_end_word:
    if len(short_string) >= 2:
        print(short_string)[0:2] + short_string[-2:]
    else:
        print(" ")

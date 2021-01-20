# # Challenge 1

def replacement(string):
    first_chars = string[0]
    return string[0] + string[1:].replace(first_chars, "$")


string = "onomatopoeia"

print(replacement(string))


# # Challenge 2

def added(list):
    return sum(list)


list = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

print(added(list))

# - We have given you a sentence, Using index/slicing please fill in the return statement so it returns "Wizards jump quickly"
def strings():
    string = "The five boxing wizards jump quickly"
    return string[16:].capitalize()


print(strings())


tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
]

print(tags[1:4:2])

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])

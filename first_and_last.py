def the_great_divide(user_string):
    _, *content, _ = user_string
    return content


print(the_great_divide(["<h1>", "some content", "</h1>"]))

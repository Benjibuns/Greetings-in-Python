# - Wow this list is crazy.  Lets see if you can solve the questions:
# - Get me the number 123
# - Get me the string 'look at me'
# - Get me the number 12
# - Get me the string 'this can get confusing
# - Get me the dictionary
# - Get me the list from the dictionary
# - If you get stuck on this its ok
crazy_list = [
    123, 40, 20,
    [
        'Hello', 'look at me',
        [
            'Holy cow', 12,
            {
                'key': 'value',
                'crazy': [
                    1, 2, 3
                ]
            }
        ]
    ],
    'what the?',
    [
        'this can get confusing'
    ]
]

print(crazy_list[0])


print(crazy_list[3][1])

print(crazy_list[3][2][1])

print(crazy_list[5][0])

print(crazy_list[3][2][2])

print(crazy_list[3][2][2]["crazy"])

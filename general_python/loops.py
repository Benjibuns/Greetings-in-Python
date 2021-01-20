# - Create an dictionary called "user". Assign it a username, email, phone and give them values.  Create 3 different for in loops.
#    - First one print out each key.
#        - Example printout:
#             - Key = > username
#             - Key = > email
#             - Key = > phone
#     - Second one print out each value.
#        - Example printout:
#             - Value = > Daniel
#             - Value = > danielfloyd@bottega.tech
#             - Value = > 888-827-9890
#     - Third one Print out each key and value.
#        - Example printout:
#             - Key = > username
#             - Value = > Daniel
#             - Key = > email
#             - Value = > danielfloyd@bottega.tech
#             - Key = > phone
#             - Value = > 888-827-9890

user_info = {
    "username": "Daniel",
    "email": "danielfloyd@bottega.tech",
    "phone": "888-827-9890",
}

for info_types in user_info.keys():
    print(info_types)

for info_type, personal in user_info.values():
    print(personal)

# for info_types, info in user.items():
#     print(info_types, ":", info)

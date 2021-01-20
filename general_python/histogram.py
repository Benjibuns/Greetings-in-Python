sales_amount = {
    "google": 50,
    "facebook": 25,
    "twitter": 10,
    "offline": 15,
}

for key, value in sales_amount.items():
    print(key[0], value * "$")


# print((list(sales_amount)[0][0]) + sales_amount["google"] * "$")
# print("f " + sales_amount["facebook"] * "$")

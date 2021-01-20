# - Create a list that has 4 types of food.  Using some built in array methods do the following:
# - Add "Bagels" to the end of the list.
# - Add "Peaches" to the start of the list.
# - Add "Green Beans" somewhere in the middle.
# - Ooops... Now replace "Green Beans" with "Pinto Beans"

list_of_foods = ["Apples", "Bananas", "Carrots", "Potatoes"]
print(list_of_foods)

list_of_foods.append("Bagels")
print(list_of_foods)

list_of_foods.insert(0, "Peaches")
print(list_of_foods)

list_of_foods.insert(3, "Green Beans")
print(list_of_foods)

list_of_foods[3] = "Pinto Beans"
print(list_of_foods)

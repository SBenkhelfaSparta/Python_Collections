# Python data collections
- Lists
- Tuples
- Dict
- Sets

Lists (Arrays in other languages)

- Shopping lists - Multiple items, add, edit, delete, update
- CRUD - `Create` `Read` `update` and `delete` 

```python
# Create a shopping list
# Syntax [] - name_of_list = ["items in list"]
shoppingList = ["apples", "egges", "chocolate", "tea", "bread"]
print(shoppingList)

# Checking what type shoppingList is
print(type(shoppingList))

# How to access chocolate
print(shoppingList[2])  # Return 3rd item in shoppingList list
print(shoppingList[-1])  # Display last item from list

# How can I replace an item in the list
shoppingList[0] = "mangos"
print(shoppingList)

# Add item to shopping list
shoppingList.append("Tuna")
print(shoppingList)

shoppingList.remove("Tuna")
print(shoppingList)

# Tuples
essentials = ("paracetamol", "milk", "water", "butter")
#essentials.pop(1) # This returns an Error as you can't change the values in tuples

# Return items 1 to 2 (last value is exclusive)
print(essentials[1:3])
```
Tuples can include any data type combinations

## Dictionaries and sets are both Data collections in python

Dictionaries and sets are both Data collections in python

Dicts are another way to manage data but can be a little more dynamic
- Dict work as KEY and VALUE
- KEY = the reference of the object
- VALUE = data that is stored for the key
- dynamic as we have Lists and another dict inside a dict
- Syntax - `name = {}`, `key = {value}`
```python
student_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["data types", "git and github", "operators", "lists and tuples"]
}

# check syntax by printing
# print(student_1)
# print(type(student_1))
print(student_1["stream"]) # accessing specific key to return value
print(student_1["completed_lessons_names"][1]) # accessing index in list value
print(student_1["completed_lessons_names"][-2])

# can we apply CRUD
student_1["completed_lessons"] = 3 # change value for key
print(student_1["completed_lessons"])

student_1["completed_lessons_names"].remove("operators") # remove item from value list
print(student_1["completed_lessons_names"])

# we have built in methods to use with dict
# to print all keys .keys()
print(student_1.keys())

# to print all values .values()
print(student_1.values())
```
## Sets are also data collection
- syntax `name = {"", "", ""}`
- sets are unordered
```python
shopping_list = ["eggs", "tea", "milk"]
print(shopping_list)
car_parts = {"engine", "wheels", "windows"}
print(car_parts) # re printing will change order in print

car_parts.add("seats")
print(car_parts)
car_parts.discard("wheels")
print(car_parts)
```

- Python also has frozen sets
- syntax `name = value([1, 2, 3, 4])`
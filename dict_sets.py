# Dictionaries and sets are both Data collections in python

# Dicts are another way to manage data but can be a little more dynamic
# Dict work as KEY and VALUE
# KEY = the reference of the object
# VALUE = data that is stored for the key
# dynamic as we have Lists and another dict inside a dict
# Syntax - name = {}, key = value

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

# Sets are also data collection
# syntax name = {"", "", ""}
# sets are unordered

shopping_list = ["eggs", "tea", "milk"]
print(shopping_list)
car_parts = {"engine", "wheels", "windows"}
print(car_parts) # re printing will change order in print

car_parts.add("seats")
print(car_parts)
car_parts.discard("wheels")
print(car_parts)
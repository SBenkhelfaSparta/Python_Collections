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
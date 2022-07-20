"""
lists
    collection of data
    can contain any/all data types in a single list
    can contain other conditions (lists, dictionaries, tuples) as list items
    mutable(items can be added, removed, or changed)
    maintain order(can use index to find an item)
"""


fruits = ["peaches","apples", "pears","apples", "apples"]
years = [3, "1998", 2.3, 987, "1994"]


# Check membership of list
print("apple" in fruits)
print("apples" in fruits)

# Check how many instances of the word "apples" is in the list
print(fruits.count("apples"))
print(fruits.count("apple"))

# Check membership as well as index position
print(fruits.index("apples"))


"""
print(fruits, years)

# Adds to the list
fruits.append("oranges")
print(fruits)

# Adds a list to the list
fruits.extend(years)
print(fruits)

# Removes "oranges" from the list. Has to be EXACT
fruits.remove("oranges")
print(fruits)

# Removes the list item according to the list index
print(fruits)
fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

# Sort can only sort with LIKE TYPES
numbers = [3, 4, 5, 6, 7, 2, 20]
numbers.sort()
print(numbers)
"""
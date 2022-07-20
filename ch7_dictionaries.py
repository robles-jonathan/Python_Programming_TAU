"""
dictionaries
    contents: key/value pairings
    mutable: can be changed
    order: maintain order of entry as of python 3.7
    syntax: curly braces contain keys and values
            keys and values seperated by a colon
            
    years = {"Layla":1974, "Ackeem":1997}
"""

stuff = {"food": 15, "energy": 100, "enemies": 13}

# Returns the value of a dictionary key 
# print(stuff.get("food"))

# Acts on entire dictionary and returns all keys and values
# print(stuff.items())

# Acts on entire dictionary and only returns keys in the dictionary
# print(stuff.keys())

"""Delete last item in the dictionary"""
# print(stuff.popitem())
# print(stuff)

"""
# Retrieves the value for a specific key and or add a new key and default value into the dictionary
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)
"""

new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

new_items = {"rocks": 2, "arrows": 5}
stuff.update(new_items)
print(stuff)

up_new = {"food": 3, "webs": 2}
stuff.update(up_new)
print(stuff)

stuff.update(food = 200, webs = 3999)
print(stuff)

stuff.update(food = 200, webs = 3999, cookies = 299999)
print(stuff)

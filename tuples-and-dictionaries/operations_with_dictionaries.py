# initialise three different dictionaries
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# print the whole dictionaries
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# print specific values by calling their key
print(dictionary['cat'])
print(phone_numbers['Suzy'])

# uses for loop to return an iterable object consisting of all the keys gathered within the dictionary
for key in dictionary.keys():
    print(key, "->", dictionary[key])

# returns tuples where each tuple is a key-value pair
for english, french in dictionary.items():
    print(english, "->", french)

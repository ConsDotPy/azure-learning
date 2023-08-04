'''Python Crash Course 3ed - Chapter 6 - Try It Yourself'''


# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city. Print
# each piece of information stored in your dictionary.
friend = {
    'first_name': 'Adrian',
    'last_name': 'Garcia',
    'age': '30',
    'city': 'Mexico City',
}
for key, value in friend.items():
    print(f"{key.title()}: {value.title()}")
# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a
# favorite number for each person, and store each as a value in your
# dictionary. Print each person’s name and their favorite number. For even
# more fun, poll a few friends and get some actual data for your program.
fav_numbers = {
    'adrian': '7',
    'yami': '3',
    'daniel': '5',
    'jose': '1',
}
for key, value in fav_numbers.items():
    print(f"{key.title()}'s favorite number is {value.title()}")
# 6-3. Glossary: A Python dictionary can be used to model an actual
# dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.
glossary = {
    'indentation': 'the space at the beginning of a line of code',
    'list': 'a collection of items in a particular order',
    'tuple': 'an immutable list',
    'dictionary': 'a collection of key-value pairs',
    'if statement': 'a conditional test that allows us to check a condition',
}

for key, value in glossary.items():
    print(f"{key.title()} is {value.title()}\n")

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

# 6-5. Rivers: Make a dictionary containing three major rivers and the
# country each river runs through. One key-value pair might
# be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    }
for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}")

for key in rivers:
    print(key.title())

for value in rivers.values():
    print(value.title())
# 6-6. Polling: Use the code in favorite_languages.py (page 96).
# • Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they
# have already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people.
# As you loop through the list, print everything you know about each person.
# Creating a list of dictionaries and duplicate each character hp and mana:
print("\nCreating a list of dictionaries and x2 each character hp and mana:")
team = [knight, wizard, paladin]
# Adding more hp and mana to each character:
for character in team:
    character['hp'] = str(int(character['hp']) * 2)
    character['mana'] = str(int(character['mana']) * 2)
    print(character)
# 6-8. Pets: Make several dictionaries, where each dictionary represents a
# different pet. In each dictionary, include the kind of animal and the
# owner’s name. Store these dictionaries in a list called pets. Next, loop
# through your list and as you do, print everything you know about each pet.
# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of
# three names to use as keys in the dictionary, and store one to three
# favorite places for each person. To make this exercise a bit more
# interesting, ask some friends to name a few of their favorite places.
# Loop through the dictionary, and print each person’s name and their favorite
# places.
# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
# each person can have more than one favorite number. Then print each
# person’s name along with their favorite numbers.
# 6-11. Cities: Make a dictionary called cities. Use the names of three
# cities as keys in your dictionary. Create a dictionary of information about
# each city and include the country that the city is in, its approximate
# population, and one fact about that city. The keys for each city’s
# dictionary should be something like country, population, and fact. Print
# the name of each city and all of the information you have stored about it.
# Dictionaries inside dictionaries:
print("\nDictionaries inside dictionaries:")
knight = {
    'hp': '100',
    'mana': '50',
    'helmet': 'royal helmet',
    'weapon': {
        'name': 'serpent sword',
        'atk': '50',
        'def': '30',
        'weight': '50.00 oz',
        },
    'shield': {
        'name': 'thorn shield',
        'atk': '0',
        'def': '60',
        'weight': '60.00 oz',
        },
    }
# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example
# programs from this chapter, and extend it by adding new keys and values,
# changing the context of the program, or improving the formatting of
# the output

'''Python Crash Course 3ed - Chapter 2 - Try It Yourself'''

# 2-1. Simple Message: Assign a message to a variable,
# and then print that message.
M = "Hello World!"
print(M)

# 2-2. Simple Messages: Assign a message to a variable, and print that message.
# Then change the value of the variable to a new message, and print the new
# message.
X = 77
print(X)
X = 88
print(X)

# 2-3. Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as,
# “Hello Eric, would you like to learn some Python today?”
NAME = "Eric"
print(f"Hello {NAME}, would you like to learn some Python today?")

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.
NAME = "eric the idle"
print(NAME.lower())
print(NAME.upper())
print(NAME.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire.
# Print the quote and the name of its author. Your output should look something
# like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried
# anything new.”
print('Voltaire once said, "I disapprove of what you say,')
print('but I will defend to the death your right to say it."')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
# person’s name using a variable called famous_person. Then compose your
# message and represent it with a new variable called message.
# Print your message.
NAME = "Voltaire"
QUOTE1 = "I disapprove of what you say,"
QUOTE2 = "but I will defend to the death your right to say it."
print(f'{NAME} once said, "{QUOTE1 + " " + QUOTE2}"')

# 2-7. Stripping Names: Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().
NAME = "\t\nAdrian\n\t"
print(NAME)

print(NAME.lstrip())
print(NAME.rstrip())
print(NAME.strip())

# 2-8. File Extensions: Python has a removesuffix() method that works exactly
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called
# filename. Then use the removesuffix() method to display the filename without
# the file extension, like some file browsers do.
FILENAME = "python_notes.txt"
print(FILENAME.removesuffix(".txt"))

# 2-9. Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8. Be sure to enclose your
# operations in print() calls to see the results.
# You should create four lines that look like this:
# print(5+3)
# Your output should be four lines, with the number 8 appearing once on each
# line.
print(5 + 3)
print(10 - 2)
print(2 * 4)
print(16 / 2)

# 2-10. Favorite Number: Use a variable to represent your favorite number.
# Then, using that variable, create a message that reveals your favorite
# number.
# Print that message.
FAV_NUM = 777
print(f"My favorite number is {FAV_NUM}.")

# 2-11. Adding Comments: Choose two of the programs you’ve written, and add at
# least one comment to each. If you don’t have anything specific to write
# because your programs are too simple at this point, just add your name and
# the current date at the top of each program file. Then write one sentence
# describing what the program does.

# 2-12. Zen of Python: Enter import this into a Python terminal session and
# skim through the additional principles.

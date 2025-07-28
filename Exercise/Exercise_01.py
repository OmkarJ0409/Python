# 1. What is the difference between input() and print() in Python?
# input() is used to take user input (always as a string).
# print() is used to display output to the screen.

# 2. How do you take integer input from the user?
num = int(input("Enter an integer: "))

# 3. What happens if you take input using input() and try to perform arithmetic directly?
# Since input() returns a string, arithmetic will result in error unless the input is converted (e.g., to int or float).

# 4. How can you take multiple inputs in a single line?
a, b = map(int, input("Enter two numbers: ").split())

# 5. How do you format output using f-strings?
name = "Alice"
print(f"Hello, {name}!")

# 6. What is the difference between f-string, % formatting, and .format()?
# f-string: Newer, cleaner: f"Hello {name}"
# % formatting: Older style: "Hello %s" % name
# .format(): Middle ground: "Hello {}".format(name)

# 7. How do you print without a newline in Python?
print("Hello", end="")

# 8. How can you print output to a file?
# with open("output.txt", "w") as file:
#     print("Hello", file=file)

# 9. What is the role of sep and end in the print() function?
# sep - sets the separator between arguments (default is space).
# end - sets what is printed at the end (default is newline).

# 10. How do you read input from a file using Python?
# with open("input.txt", "r") as file:
#     data = file.read()

# 11. What is dynamic typing in Python?
# Python automatically infers the variable type at runtime.

# 12. How do you declare and assign a variable in Python?
x = 10

# 13. What are the standard data types available in Python?
# int, float, str, bool, list, tuple, dict, set, NoneType, complex

# 14. What is the difference between mutable and immutable types? Give examples.
# Mutable: Can be changed (e.g., list, dict)
# Immutable: Cannot be changed (e.g., int, str, tuple)

# 15. What happens when you assign one variable to another?
# Both variables refer to the same object in memory.

# 16. How do you check the data type of a variable?
type(x)

# 17. What is the difference between int, float, and complex in Python?
# int: Whole numbers
# float: Decimal numbers
# complex: Numbers with imaginary parts (e.g., 3 + 4j)

# 18. What is NoneType in Python?
# A special type representing "no value". Example: x = None

# 19. How do Python variables handle memory?
# Python uses reference counting and garbage collection to manage memory.

# 20. Can we use reserved keywords as variable names?
# No. Doing so results in a SyntaxError.

# 21. What are different types of operators in Python?
# Arithmetic, Assignment, Comparison, Logical, Bitwise, Membership, Identity

# 22. How is == different from is?
# == compares values
# is checks whether two variables refer to the same object

# 23. What is the use of // and % operators?
# //: Floor division (returns quotient without decimal)
# %: Modulus (returns remainder)

# 24. Explain bitwise operators in Python with examples.
# a = 5  # 0101
# b = 3  # 0011
# a & b  # 0001 -> 1
# a | b  # 0111 -> 7
# a ^ b  # 0110 -> 6
# ~a     # Inverts all bits

# 25. What is the output of True + True and why?
# True — because True is treated as 1 in numeric context.

# 26. Explain operator precedence with an example.
# result = 3 + 4 * 2  # Output: 11

# 27. How do comparison operators work in Python?
# They return True or False after comparing values using ==, !=, <, >, etc.

# 28. What are identity and membership operators?
# Identity: is, is not
# Membership: in, not in

# 29. What is short-circuit evaluation in logical operators?
# Evaluation stops as soon as the result is determined.
# Example: True or function() → function not called.

# 30. Can we overload operators in Python?
# Yes, using special methods like __add__, __eq__, etc.

# 31. What is the syntax of if statements in Python?
# if condition:
    # statement

# 32. How does if-else work in Python?
# Executes one block if the condition is true, else another.

# 33. What is the role of elif and how is it different from nested if?
# elif avoids deep nesting and is more readable.

# 34. Give a real-world example using nested if-else conditions.
age = 25
if age > 18:
    if age < 60:
        print("Adult")

# 35. How does Python evaluate chained comparison like 3 < x < 7?
# As: 3 < x and x < 7

# 36. What happens if indentation is not correct in control statements?
# Python raises an IndentationError.

# 37. Is it necessary to use else after if?
# No. if can be used alone.

# 38. What is the output of if 0: and why?
# No output — 0 is false.

# 39. Can we write if condition without a block?
# No, at least one statement is required (use pass if needed).

# 40. How do you handle multiple conditions in a single if?
# Use logical operators:
if a > 0 and b > 0:
    print("Both positive")

# 41. What are different ways to create strings in Python?
# 'Hello', "Hello", '''Hello''', """Hello"""

# 42. How are strings stored in memory in Python?
# As immutable sequences of Unicode characters.

# 43. What is the difference between single, double, and triple quotes?
# Single/double: for single-line
# Triple: for multi-line strings

# 44. How can you concatenate and repeat strings?
# "Hello" + " World"
# "Hi" * 3 → "HiHiHi"

# 45. What are string slicing and indexing? Give examples.
s = "Python"
s[0]   # 'P'
s[1:4] # 'yth'

# 46. How do you reverse a string in Python?
s[::-1]

# 47. Are strings mutable in Python?
# No, they are immutable.

# 48. What is the use of join() and split()?
# join(): Combine list into string
# split(): Split string into list

# 49. What does strip(), lstrip(), and rstrip() do?
# strip(): removes whitespace from both ends
# lstrip(): from left
# rstrip(): from right

# 50. How can you find if a substring exists in a string?
# 'sub' in 'string'

# 51. How do you count occurrences of a character in a string?
s.count('a')

# 52. What is the use of find() and index()?
# find(): returns index or -1 if not found
# index(): raises an error if not found

# 53. How can you replace a part of a string?
s.replace("old", "new")

# 54. How to format strings using .format()?
"Hello {}".format("World")

# 55. What are escape sequences in strings?
# Special characters prefixed with \
# Example: \n, \t, \\, \', \"

# 56. What are escape sequences? List 5 common ones.
# \n: newline
# \t: tab
# \\: backslash
# \': single quote
# \": double quote

# 57. Difference between \n, \r, and \t?
# \n: Newline
# \r: Carriage return
# \t: Tab space

# 58. How do you print a backslash (\) in a string?
print("\\")

# 59. How does \b behave in Python string?
# Backspace — removes the character before it in output (may not work well in all consoles).

# 60. Can you use escape characters in raw strings?
# No. In raw strings, escape characters are not processed:
# r"\n" prints as \n

# 61. What is a dictionary in Python?
# A dictionary is an unordered collection of key-value pairs. Example:
d = {"name": "Alice", "age": 25}

# 62. How do you create a dictionary?
d = dict()
d = {"a": 1, "b": 2}

# 63. How can you access, add, or update values in a dictionary?
d["key"] = "value"  # add or update
value = d["key"]    # access

# 64. What happens when you access a key that doesn’t exist?
# Raises a KeyError.

# 65. What is the difference between get() and direct access?
# d["key"] raises error if key is missing
# d.get("key") returns None or default value

# 66. How do you iterate over dictionary keys and values?
for k, v in d.items():
    print(k, v)

# 67. How to merge two dictionaries?
# merged = {**dict1, **dict2}  # or dict1.update(dict2)

# 68. What is dictionary comprehension? Give an example.
squares = {x: x**2 for x in range(5)}

# 69. How do you delete a key from a dictionary?
del d["key"]

# 70. Can dictionary keys be mutable? Why or why not?
# No. Dictionary keys must be immutable and hashable (e.g., str, int, tuple).

# 71. What is a set in Python?
# A set is an unordered collection of unique elements.

# 72. How do you create a set?
s = {1, 2, 3}
s = set([1, 2, 3])

# 73. What is the difference between set and list?
# Set: unordered, no duplicates
# List: ordered, allows duplicates

# 74. How do you add and remove elements from a set?
s.add(4)
s.remove(1)

# 75. What are set operations: union, intersection, difference, symmetric difference?
# a | b: union
# a & b: intersection
# a - b: difference
# a ^ b: symmetric difference

# 76. How are duplicates handled in sets?
# Automatically removed. Each element is unique.

# 77. How to check if a set is a subset/superset of another?
# a.issubset(b)
# a.issuperset(b)

# 78. What is a frozen set?
# An immutable version of a set:
# fs = frozenset([1, 2, 3])

# 79. Can we use set elements as dictionary keys?
# Only if the elements are immutable (e.g., strings, numbers).

# 80. How to iterate through a set?
for item in s:
    print(item)

# 81. What is a tuple? How is it different from a list?
# Tuple: Immutable sequence
# List: Mutable sequence

# 82. How do you create a tuple with a single element?
t = (1,)  # comma is necessary

# 83. Are tuples mutable or immutable?
# Immutable.

# 84. How can you convert a list to a tuple?
tuple([1, 2, 3])

# 85. How to access elements in a tuple?
# t[0], t[1], t[-1]

# 86. What is tuple unpacking? Give an example.
a, b = (1, 2)

# 87. Can a tuple contain mutable elements?
# Yes. Tuples can contain lists or dictionaries as elements.

# 88. How do you iterate through a tuple?
for item in t:
    print(item)

# 89. When should you use a tuple over a list?
# When the data should not change or be used as a dictionary key.

# 90. How can you concatenate or repeat tuples?
# t1 + t2
# t1 * 3

# 91. What is type casting in Python?
# Converting one data type to another.

# 92. How do you convert string to int, float to int, etc.?
# int("10"), float("5.6"), str(5)

# 93. What is the difference between int("3.14") and float("3.14")?
# int("3.14") → error
# float("3.14") → 3.14

# 94. How do you safely cast input values using try-except?
try:
    val = int(input())
except ValueError:
    print("Invalid input")

# 95. How do you convert list to tuple and vice versa?
# tuple([1, 2, 3])
# list((1, 2, 3))

# 96. What will be the output of:
a = "5"
b = 2
print(a * b)
# Answer: '55' — string "5" repeated 2 times.

# 97. How can you count characters in a string using dictionary?
def count_characters(s):
    char_count = {}  # Initialize an empty dictionary
    for char in s:
        if char in char_count:
            char_count[char] += 1  # Increment count if char is already in the dictionary
        else:
            char_count[char] = 1   # Add new char to dictionary with count 1
    return char_count

text = "hello world"
result = count_characters(text)
print(result)


# 98. Write a program to check if a number is positive, negative, or zero.
number = 1
if number == 0:
    print("It's Zero")
elif number > 0:
    print("It's Positive")
else:
    print("It's Negative")

# 99. What’s the output of:
x = None
if x:
    print("True")
else:
    print("False")    
# Answer: False — because None is false.

# 100. How would you write a program to categorize marks using nested if-else?
marks = 97
if marks > 90:
    if marks >= 95:
        print("A+")
    else:
        print("A")
elif marks > 80:
    if marks >= 85:
        print("B+")
    else:
        print("B")
elif marks > 70:
    if marks >= 75:
        print("C+")
    else:
        print("C")
else:
    print("D")
# Data Types Practice
# This file is for learning how to check data types in Python
# Learning: How to identify what type of data you are working with
# Date: June 2026

# The type() function is used to check the data type of any value
# Syntax: type(value)

# Example 1: Check type of a float (decimal number)
# Float is a number with decimal point
print("Example 1: Checking float type")
my_number = 3.0
print(type(my_number))  # Output: <class 'float'>
print()

# Example 2: Check type of an integer (whole number)
# Integer is a whole number without decimal point
print("Example 2: Checking integer type")
my_age = 25
print(type(my_age))  # Output: <class 'int'>
print()

# Example 3: Check type of a string (text)
# String is text enclosed in quotes
print("Example 3: Checking string type")
my_name = "Yosep"
print(type(my_name))  # Output: <class 'str'>
print()

# Example 4: Check type of a boolean (true or false)
# Boolean is a value that is either True or False
print("Example 4: Checking boolean type")
is_student = True
print(type(is_student))  # Output: <class 'bool'>
print()

# Example 5: Check multiple different types
# You can check different types in one program
print("Example 5: Checking multiple types")
print(type(3.14))        # float
print(type(100))         # int
print(type("hello"))     # string
print(type(False))       # bool
print()

# Example 6: Create a function to check data type
# This function helps us organize our code better
def check_data_type(value):
    """
    This function checks and returns the data type of any value
    Parameter: value - any data you want to check
    Returns: the data type of that value
    """
    return type(value)

# Use the function with different values
print("Example 6: Using a function to check data type")
print(check_data_type(3.0))      # <class 'float'>
print(check_data_type(3))        # <class 'int'>
print(check_data_type("Yosep"))  # <class 'str'>
print(check_data_type(True))     # <class 'bool'>
print()

# Example 7: Create a function like SoloLearn exercise
# This is similar to the balance() function example
def balance(amount):
    """
    This function returns the type of the amount parameter
    It helps us understand what kind of number we are working with
    """
    return type(amount)

# Test the balance function
print("Example 7: Using balance() function")
print(balance(3.0))      # <class 'float'>
print(balance(100))      # <class 'int'>
print(balance(50.5))     # <class 'float'>
print()

# Example 8: Check type of different number formats
print("Example 8: Different number formats")
print(type(42))          # integer
print(type(3.14159))     # float
print(type(1e5))         # float (scientific notation)
print(type(-15))         # integer (negative number)
print(type(-2.5))        # float (negative decimal)
print()

# Example 9: Practical example - Banking
# Imagine a banking system that needs to check data types
def deposit(account_holder, amount):
    """
    This function simulates a bank deposit
    It checks the types of inputs to make sure they are correct
    """
    print(f"Account holder: {account_holder}")
    print(f"Type of account holder: {type(account_holder)}")  # Should be string
    print(f"Amount: {amount}")
    print(f"Type of amount: {type(amount)}")  # Should be float or int
    print()

# Use the deposit function
print("Example 9: Banking system example")
deposit("Muhammad Yosep", 1000.50)
print()

# Example 10: Challenge Exercise
# Try to predict the output before running
print("Example 10: Challenge - What type is this?")
mystery_value = "42"
print(type(mystery_value))  # Is this a number or string?
print()

# Explanation:
# "42" with quotes is a STRING, not a number!
# 42 without quotes is an INTEGER

# Practice Exercises:
# 1. Create a variable with your age (integer)
# 2. Create a variable with your height (float)
# 3. Create a variable with your name (string)
# 4. Create a variable with your student status (boolean)
# 5. Check the type of each variable using type()
# 6. Create a function that takes all four values as parameters
#    and prints their types

print("=== Your Practice Starts Here ===")
print("Create your own variables and check their types!")
print()

# Start your practice:
my_age = 25
my_height = 170.5
my_name = "Yosep"
am_i_student = True

print(f"My age: {my_age}, Type: {type(my_age)}")
print(f"My height: {my_height}, Type: {type(my_height)}")
print(f"My name: {my_name}, Type: {type(my_name)}")
print(f"Am I student: {am_i_student}, Type: {type(am_i_student)}")

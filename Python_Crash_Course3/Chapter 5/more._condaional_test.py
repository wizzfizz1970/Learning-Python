'''5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() function
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''


# Tests for equality and inequality with strings
print("apple" == "apple")  
print("apple" != "orange")  
print("Apple" == "apple")  

# Tests using the lower() function
print("APPLE".lower() == "apple")  
print("ORANGE".lower() == "Orange")  

# Numerical tests involving equality, inequality, and comparisons
number = 10
print(number == 10)  
print(number != 5)  
print(number > 5)  
print(number < 20)  
print(number >= 10)  
print(number <= 9)  

# Tests using the and keyword and the or keyword
age = 25
print(age > 20 and age < 30)  
print(age > 30 or age < 20)  

# Test whether an item is in a list
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  
print("grape" in fruits)  

# Test whether an item is not in a list
print("grape" not in fruits)  
print("banana" not in fruits)  

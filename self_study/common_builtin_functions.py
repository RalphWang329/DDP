# 1. print(): Prints the specified message to the screen.
print("Hello, world!")

# 2. input(): Reads input from the user as a string.
name = input("Enter your name: ")

# 3. len(): Returns the length of an object (e.g., string, list).
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # Output: 5

# 4. type(): Returns the type of an object.
num = 10
print(type(num))  # Output: <class 'int'>

# 5. range(): Generates a sequence of numbers within a specified range.
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# 6. str(): Converts an object into a string.
num = 10
num_str = str(num)
print(num_str)  # Output: '10'

# 7. int(): Converts a string or number to an integer.
num_str = "10"
num = int(num_str)
print(num)  # Output: 10

# 8. float(): Converts a string or number to a floating-point number.
num_str = "3.14"
num = float(num_str)
print(num)  # Output: 3.14

# 9. list(): Converts an iterable (e.g., tuple) to a list.
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

# 10. tuple(): Converts an iterable (e.g., list) to a tuple.
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# 11. dict(): Creates a new dictionary.
my_dict = dict(name='John', age=30)
print(my_dict)  # Output: {'name': 'John', 'age': 30}

# 12. max(): Returns the largest element in an iterable.
nums = [10, 20, 30]
max_num = max(nums)
print(max_num)  # Output: 30

# 13. min(): Returns the smallest element in an iterable.
nums = [10, 20, 30]
min_num = min(nums)
print(min_num)  # Output: 10

# 14. sum(): Returns the sum of all elements in an iterable.
nums = [1, 2, 3, 4, 5]
total = sum(nums)
print(total)  # Output: 15

# 15. abs(): Returns the absolute value of a number.
num = -10
abs_num = abs(num)
print(abs_num)  # Output: 10

# 16. round(): Rounds a number to a specified number of decimal places.
num = 3.14159
rounded_num = round(num, 2)
print(rounded_num)  # Output: 3.14

# 17. sorted(): Returns a sorted list of the specified iterable.
nums = [3, 1, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # Output: [1, 2, 3]

# 18. enumerate(): Returns an enumerate object containing the index and value of each item in an iterable.
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(index, value)  # Output: 0 a, 1 b, 2 c

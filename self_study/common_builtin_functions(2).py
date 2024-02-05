# 19. zip(): Combines two or more iterables element-wise into tuples.
nums = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(nums, letters)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# 20. any(): Returns True if any element in an iterable is true, otherwise False.
nums = [0, 1, 2, 3]
print(any(nums))  # Output: True

# 21. all(): Returns True if all elements in an iterable are true, otherwise False.
nums = [1, 2, 3]
print(all(nums))  # Output: True

# 22. reversed(): Returns a reverse iterator for an iterable.
nums = [1, 2, 3]
reversed_nums = reversed(nums)
print(list(reversed_nums))  # Output: [3, 2, 1]

# 23. isinstance(): Checks if an object is an instance of a specified class.
num = 10
print(isinstance(num, int))  # Output: True

# 24. chr(): Returns the character that corresponds to the specified Unicode code.
print(chr(65))  # Output: 'A'

# 25. ord(): Returns the Unicode code of a specified character.
print(ord('A'))  # Output: 65

# 26. map(): Applies a function to all the items in an input list.
nums = [1, 2, 3]
squared = map(lambda x: x**2, nums)
print(list(squared))  # Output: [1, 4, 9]

# 27. filter(): Filters elements from an iterable based on a function.
nums = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, nums)
print(list(even))  # Output: [2, 4]

# 28. dir(): Returns a list of valid attributes for an object.
my_list = [1, 2, 3]
print(dir(my_list))  # Output: ['__add__', '__class__', '__contains__', ...]

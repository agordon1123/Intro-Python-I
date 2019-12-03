"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]
# i [0, 1, 2, 3, 4, 5]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
# stl = second-to-last
stl = len(a) -2
print(a[stl])

# Output the last three elements in the array: [7, 9, 6]
print(a[3:])

# Output the two middle elements in the array: [1, 7]

# 1: Trying to solve if list is mutated
upperindex = int(len(a) / 2) + 1
print(upperindex)
lowerindex = upperindex -1
print(lowerindex)
print(a[lowerindex:upperindex + 1])

# 2: Simply solving the request
print(a[3:5])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])
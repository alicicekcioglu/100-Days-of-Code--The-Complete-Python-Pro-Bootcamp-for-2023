# List and Comprehensions: It is a case where you create a new list from a previous list.

numbers = [1, 2, 3]
new_list = []
# with for loop
for i in numbers:
    add_1 = i+1
    new_list.append(add_1)

# How to create list comprehension: new_list = [new_item for i in list]
new_list = [i + 1 for i in numbers]
print(new_list)

# How to create list comprehension: new_list = [letter for letter in name]
name = "Angela"
new_list1 = [letter for letter in name]
print(new_list1)

# Example
a = [i*2 for i in range(1, 5)]
print(a)

# Conditional list comprehension: new_item = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [i.upper() for i in names if len(i) >= 5]
print(long_names)
short_names = [i for i in names if len(i) <= 4]
print(short_names)
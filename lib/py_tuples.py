t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)

my_data = ({'name': 'Alice', 'age': 25}, ['apple', 'banana', 'cherry'], ('red', 'green', 'blue'))

# Access the first element of the tuple (the dictionary)
my_dict = my_data[0]
print(my_dict['name'])  # Output: 'Alice'

# Access the second element of the tuple (the list)
my_list = my_data[1]
print(my_list[0])  # Output: 'apple'

# Access the third element of the tuple (the tuple)
my_tuple = my_data[2]
print(my_tuple[1])  # Output: 'green'

my_data[0]['age'] = 30  # Update the age value in the dictionary
print(my_data[0]['age'])  # Output: 30

my_data[1][0] = 'orange'  # Update the first value in the list
print(my_data[1][0])  # Output: 'orange'

# This will raise a TypeError because tuples are immutable
my_data[2][0] = 'yellow'
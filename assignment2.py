#Edward McBride
#CIS103
#Assignment 2
#Proffesor MD Ali
#This code performs a while loop and before the numbers get to 6 it breaks the loop.
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
#This code performs a for loop and it also prints each character with its ASCII value.
test_list = ['CIS103']
print('The original list : '+str(test_list))
res = []
for ele in test_list:
    res.extend(ord(num) for num in ele)
print('The ascii list is :' + str(res))
#This section of the code will print a nested loop that will show a star pattern
for i in range(1, 5):
    for j in range(i):
        print('*', end='')
    print()
#This portion of the code will take a string and return it in reverse due to slicing.
def reverse_string(string):
    'Reverses a string using slicing.'
    return string[::-1]
my_string = 'Hello, World!'
reversed_string = reverse_string(my_string)
print(reversed_string)
#This portion of the code will format the following output for the given variables.
name = 'John'
age = 30
salary = 50000.50
message = 'My name is {0} and I am {1} years old. My salary is {2} per year.'.format(name,age,salary)
print(message)
#This portion of the code will handle different things with a list of integers and the different operations.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.append(10)
my_list.insert(2, 11)
my_list.sort()
my_list.remove(11)
del my_list[6]
print(my_list)
#This part of the code will create a tuple and I will try to also change one of the elements.
my_tuple = (1, 'yoo', 75, True, 65)
print(my_tuple[0:2])
#When I changed the one element, nothing really changed.
#This portion of the code I am going to create a dictionary.
my_dict = { 'name': 'John', 'age': 30, 'city': 'New York'}
my_dict['occupation'] = 'Driver'
my_dict['age'] = 43
del my_dict['city']
for key, value in my_dict.items():
    print(key, ':', value)
#This portion of the code uses a 'while' loop and will break it when a certain condition isnt met.
count = 125
while count < 175:
    count += 1
    if (count % 130) == 0:
        continue
    print(count)
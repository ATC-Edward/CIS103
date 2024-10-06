#Edward McBride
#CIS103
#Date: 10/5/24
#Proffessor MD ALI
#This code will work through many different ways of handling data.
#I will be creating a blank list and name it fruits
fruits = []
#I am going to create an list and name it fruits.
fruits = ['apple', 'banana', 'orange', 'grape']
print(fruits)
#I am now going to remove the element banana from the list and print it to show the changes.
fruits.remove('banana')
print(fruits)
#I am now going to add the element strawberry to my list and print to show that it was added.
fruits.append('strawberry')
print(fruits)
#I am now going to create a tuple and name it colors
colors = ('red', 'green', 'blue', 'yellow')
#I am now going to print the tuple
print(colors)
#I am now going to program where the tuple will only print the first and last elements of the tuple
print(colors[0])
print(colors[3])
#I will now demonstrate trying to remove data from a tuple and how the computer wont allow you because a tuple is not able to be modified

#I am now going to be creating a set and modifying it
student_names = {'John', 'Emma', 'Sophia', 'James'}
print(student_names)
#I am now going to add the name Oliver to the set
student_names.add('Oliver')
print(student_names)
#I am now going to remove the name Sophia from the set
student_names.remove('Sophia')
print(student_names)
#I will try to add the name John again to the set
student_names.add('John')
print(student_names)
#After trying to add John again it simply just printed the code without duplicating the name. Sets are designed to store unique elements and cant duplicate multiple of the same element.
#Next I will be adding a code for the dictionary function in Python
student_scores = {'John': 85,'Emma': 92,'Sophia': 78,'James': 89}
print(student_scores)
#Now I will just print Emma's score
print(student_scores['Emma'])
#Now I will be adding a new student and their test grades
student_scores['Oliver'] = 95
print(student_scores)
#Now I am going to update Sophia's score to 82
student_scores['Sophia'] = 82
print(student_scores)
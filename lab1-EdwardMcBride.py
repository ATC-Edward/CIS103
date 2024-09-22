#
#Lab1: Getting Started with Python
#CIS 103: Introduction to Programming
#Instructor: Edward McBride
#Student name: Edward McBride
#Date: 9/7/24
#Description:
#This script prints a personalized greeting message
#and demonstrates the use of variables and basic data types.
#
#get the user's name(string)and age (integer)
name=input("Enter your name:")
age=int(input("Enter your age:"))
#Calculate the year the user was born
current_year=2024
birth_year=current_year-age
#print a personalized greeting message
print(f"Hello,{name}!You were born in{birth_year}.")

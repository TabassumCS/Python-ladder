"""Comparison operators:

== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to"""

"""Write a program that:
1. Asks the user for their age
2. Prints a message based on their age:
   - If age is less than 13: "You are a child"
   - If age is 13 to 17: "You are a teenager"
   - If age is 18 to 59: "You are an adult"
   - If age is 60 or more: "You are a senior"""

age = int(input("How old are you? "))

if age <= 13:
    print("You are a child")
elif age <= 17:
    print("You are a teenager")
elif age <=59:
    print("You are an adult")
else:
    print("You are a senior")

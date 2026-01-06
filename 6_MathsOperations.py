"""Simple Calculator
Write a program that:
1. Asks the user for a number (first number)
2. Asks the user for another number (second number)
3. Calculates and prints:
   - The sum (addition)
   - The difference (subtraction)
   - The product (multiplication)"""

first_number = int(input("Please enter a number: "))
second_number = int(input("Please enter another number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

print(f"Sum: {addition}\nDifference: {subtraction}\nProduct: {multiplication}")

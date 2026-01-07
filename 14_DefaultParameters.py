#Sometimes you want a function to have a default value if the user doesn't provide one.
"""
Without default parameters:
pythondef greet(name):
    print(f"Hello, {name}!")

greet("Tabassum")  # Works
greet()            # ERROR! Missing required argument
With default parameters:
pythondef greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Tabassum")  # Hello, Tabassum!
greet()            # Hello, Guest!
If you don't pass a value, it uses the default!

Multiple parameters with defaults:
pythondef introduce(name, age=18, city="London"):
    print(f"I'm {name}, {age} years old, from {city}")

introduce("Sam")                      # I'm Sam, 18 years old, from London
introduce("Tabassum", 24)             # I'm Tabassum, 24 years old, from London
introduce("Alex", 30, "Manchester")   # I'm Alex, 30 years old, from Manchester

Important rule: Parameters with defaults must come after parameters without defaults!
python# WRONG
def greet(name="Guest", age):  # ERROR!
    print(f"Hello {name}, age {age}")

# CORRECT
def greet(age, name="Guest"):
    print(f"Hello {name}, age {age}")
```"""


"""Write a program that:
1. Creates a function called `power(base, exponent=2)` with a default exponent of 2
2. The function calculates base raised to the exponent (use `**` operator)
3. Returns the result
4. Test it three ways:
   - Call with just one number (should square it)
   - Call with two numbers (should calculate power)
   - Ask user for input and use the function"""

def power(base, exponenet=2):
    result = base**exponenet
    return result

print(power(4))
print(power(5,3))
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = power(base, exponent)
print(f"Result:{result}")
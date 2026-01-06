#For loops are used when you know how many times you want to repeat something.

"""for i in range(5):
    print(i)
```

This prints:
```
0
1
2
3
4
Notice it starts at 0 and goes up to (but not including) 5!
Starting at 1:
pythonfor i in range(1, 6):
    print(i)
This prints: 1, 2, 3, 4, 5"""

#The pattern: range(start, stop) goes from start up to (but not including) stop.

"""Using the loop variable in calculations:
pythonfor i in range(1, 6):
    result = i * 2
    print(f"{i} times 2 equals {result}")
```

This prints:
```
1 times 2 equals 2
2 times 2 equals 4
3 times 2 equals 6
4 times 2 equals 8
5 times 2 equals 10
Looping through text:
pythonname = "Sam"
for letter in name:
    print(letter)
```

This prints each letter on a new line: `S`, `a`, `m`
"""

"""Write a program that:
1. Asks the user for a number
2. Prints the multiplication table for that number from 1 to 10"""

num = int(input("Enter a number: "))

for i in range(1, 11):
    result = i*num
    print(f"{num} x {i} = {result}")
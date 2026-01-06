"""Sometimes we want to repeat code multiple times. Loops let us do this!
While loop - repeats as long as a condition is True

ount = 1

while count <= 5:
    print(f"Count is: {count}")
    count = count + 1
```

This prints:
```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5

How it works:

Check if condition is True (count <= 5)
If True, run the code inside
Go back to step 1
If False, stop

Important: Always change the variable inside the loop, or it runs forever!"""

"""Write a program that:
1. Asks the user for a number
2. Counts DOWN from that number to 1
3. Prints "Blast off!" at the end"""



count = int(input("Enter a number: "))

while count >= 1:
    print(f"Count is: {count}")
    count = count - 1

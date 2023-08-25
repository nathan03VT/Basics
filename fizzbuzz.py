#!/usr/bin/python3

for num in range(1,21):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz", end="")
    elif num % 3 == 0:
        print("Fizz", end="")
    elif num % 5 == 0:
        print("Buzz", end="")
    else:
        print(num, end="")

    if num != 20:
        print(", ", end="")
    else:
        print("\n")        

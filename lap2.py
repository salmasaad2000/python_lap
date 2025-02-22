#!/usr/bin/python
#------------------------Q1--------------------------------#
print("\n-----------------------------Q1---------------------------------\n")

operation= input("Enter operation: ")
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

match operation:
        case "+":
            print( a + b)
        case "-":
            print( a - b )
        case "*":
            print( a * b )
        case "/":
            print( a / b if b != 0 else "Error: Division by zero")
        case _:
            print( "Invalid operation")

#--------------------------Q2--------------------------------#
print("\n------------------------------Q2--------------------------------\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = [num for num in numbers if num % 2 != 0]
count = len(odd_numbers)

print(odd_numbers, "Count =", count)


#--------------------------Q3--------------------------------#
print("\n-------------------------------Q3-------------------------------\n")

password = input("Enter your password: ")

if (
    len(password) >= 8
    and any(char.isupper() for char in password)
    and any(char.isdigit() for char in password)
):
    print("Valid Password")
else:
    print("Invalid Password")


#--------------------------Q4--------------------------------#
print("\n---------------------------------Q4-----------------------------\n")

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {**dic1, **dic2, **dic3}

print(result)


#--------------------------Q5--------------------------------#
print("\n--------------------------------Q5------------------------------\n")

s = input("Enter string: ")

longest = current = s[0]

for i in range(1, len(s)):
    if s[i] >= s[i - 1]:
        current += s[i]
    else:
        if len(current) > len(longest):
            longest = current
        current = s[i]

if len(current) > len(longest):
    longest = current

print("Longest substring in alphabetical order is:", longest)


#--------------------------Q6--------------------------------#
import re
print("\n-------------------------------Q6-------------------------------\n")
email = input("Entar Email: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

#!/usr/bin/python
#-----------Q1----------------#
a = [10, 20, 30, 20, 40, 50]
a.remove(20)
print("<----------------------------Q1----------------------------->")
print(a)


#-----------Q2----------------#
a = [10, 20, 30, 20, 40, 50]
val = a.pop(1)  
print("<--------------------------Q2------------------------------->")
print("Removed value:", val)
print("Updated list:", a)


#-----------Q3----------------#
a = [10, 20, 30, 40, 50, 60, 70]
del a[1:4] 
print("<----------------------------Q3--------------------------->")
print(a)



#-----------Q4----------------#
a = [10, 20, 30, 40, 50, 60, 70]
a.clear()
print("<----------------------------Q4---------------------------->")
print(a)




#-----------Q5----------------#
x = "iti"
count = x.count("i")
print("<---------------------------Q5---------------------------->")
print(count)



#-----------Q6----------------#
print("<---------------------------Q6----------------------------->")
binary_num = input("Enter a binary number: ")
decimal_num = int(binary_num, 2)
print("Decimal value:", decimal_num)


#-----------Q7----------------#
print("<---------------------------Q7----------------------------->")
num = int(input("Enter your number: "))
if (num%3 ==0 and num%5 ==0):
    print("fizbuz")
elif (num%3 ==0 ):
    print("fizz")
elif (num%5 ==0):
    print("buzz")
else:
    print("not divisible by 3 nor 5")       
#-----------Q8----------------#
print("<--------------------------Q8------------------------------>")
radius =  int(input("Enter reduice of circle: "))
import math

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")

#-----------Q9----------------#
print("<--------------------------Q9------------------------------>")

while True:
    name = input("Enter your name: ").strip()
    if name.isalpha() and name != "":
        break
    else:
        print("Invalid input! Please enter a valid name (letters only).")

email = input("Enter your Email: ")

print(f"your data :\nName: {name}\nEmail: {email}")



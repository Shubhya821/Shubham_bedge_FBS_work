a = int(input("enter the first number:"))
b= int (input("enter the second number:"))
c = int(input("enter the third number:"))

if a > b:
    if a >c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c

print("The maximum number ", max)
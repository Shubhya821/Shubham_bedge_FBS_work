num = int (input("enter the number :"))
i = 1
sum = 0

while (i < num ):
     if num % i == 0:
        sum +=i
     i = i+1 

if sum == num:
     
     print("number is perfect number ")
else:
     print("number is not perfect:")
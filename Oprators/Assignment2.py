# 1. Convert the time entered in hh,min and sec into seconds.

# hh = int(input("enter the hours "))
# mm = int(input("enter the mm"))
# ss = int(input("enter the second "))

# second = (hh * 3600) + (mm * 60 ) + ss

# print("the time entered in second is ", second)


# 2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# c = int(input("enter the degree celcius "))

# f = ((c / 5 ) * 9 ) + 32

# print("the celcius to faheniheit is ", f)

# 3. Convert distant given in feet and inches into meter and centimeter.

# feet = int (input("enter the feet "))
# inches = int(input("enter the inches "))


# total_inches  = (feet * 12) + inches

# centimeter =  total_inches * 2.54
# meter = centimeter / 100


# print("distance in meter and centimeter is ", meter , "meter", centimeter , "centimeter")


# # 4. WAP to calculate area of triangle and rectangle

# len = int(input("enter the length"))
# bredth = int(input("enter the bredth"))
# base = int(input("enter the base"))
# height = int(input("enter the height"))

# area_triangle = (0.5 * base * height)

# area_react = len * bredth


# print("the area of triangle is ", area_triangle , "and area of rectangle is", area_react)


# # 5. WAP to calculate selling price of book based on cost price and discount.

# cost = int(input("enter the cost price"))
# dis  = int(input("enter the discount "))


# selling_price = cost - (dis /100) * 100

# print("selling price is ", selling_price)

# Q6. WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

# basic_sal = int(input("enter the salary "))

# total_sal = basic_sal + ((10 / 100) * basic_sal) + ((12 / 100) * basic_sal ) + ((15 / 100) * basic_sal )

# print("total salary is ", total_sal)


# 7. Find the sum of three-digit number.

# num = int(input("enter the number ")) 

# r1 = num % 10  #5
# quo = num // 10 #14

# r2 = quo % 10 #4
# quo = quo // 10  #1

# sum = r1 + r2 + quo

# print("the sum of three digit is ", sum)


# Q8. Write a program to swap two numbers with using third variable.

# a = int(input("enter the first number "))
# b = int(input("enter the second number "))

# temp = a

# a = b

# b= temp

# print("two swappned number are ", a, b)


# # 9. Write a program to swap two numbers without using third variable.

# a = int(input("enter the first number "))
# b = int(input("enter the second number "))

# a , b = b , a 

# print("swap number is ", a , b )

# 10. Write a program to reverse three-digit number.123

# num = int(input ("enter the three digit number :"))

# num1 = num % 10 #3 
# num = num // 10  #12

# num2= num % 10 #2

# num3 = num // 10 #1


# sum = (num1 * 100) + (num2 *10) + num3

# print("the reverse numbers are " , sum)


# 11. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.

# amount = int(input("enter the amount "))

# n2000 = amount // 2000
# amount = amount % 2000

# n500 = amount // 500
# amount = amount % 500

# n200 = amount // 200
# amount = amount % 200

# n100 = amount // 100
# amount = amount % 100

# n50 = amount // 50
# amount = amount % 50

# n20 = amount // 20
# amount = amount % 20

# n10 = amount // 10
# amount = amount % 10

# n5 = amount // 5
# amount = amount % 5

# n2 = amount // 2
# amount = amount % 2

# n1 = amount // 1
# amount = amount % 1

# print("notes")
# print("₹2000 =", n2000)
# print("₹500  =", n500)
# print("₹200  =", n200)
# print("₹100  =", n100)
# print("₹50   =", n50)
# print("₹20   =", n20)
# print("₹10   =", n10)
# print("₹5    =", n5)
# print("₹2    =", n2)
# print("₹1    =", n1)


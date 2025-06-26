# # Q1. write a programe to calculate the percentage of student based on marks of any 5 subject 

# M1 = int (input("enter the marks of first subject:"))
# M2 = int (input("enter the marks of second subject:"))
# M3 = int (input("enter the marks of third subject:"))
# M4 = int (input("enter the marks of fourth subject:"))
# M5 = int (input("enter the marks of fifth subject:"))


# total_marks = M1 + M2 + M3 + M4 + M5

# total_percent = (total_marks / 500) * 100

# print("Total percentage is :", total_percent)


# Q2.Write a program to calculate area of rectangle based on length and breadth.

# l = int(input("enter the length :"))
# b = int(input("enter the breadth :"))

# area_rect = l * b

# print("area of reactangle is :" , area_rect)



# Q3. Program to find quotient and remainder of two numbers.

# num_1 = int (input("enter the first number:"))
# num_2 = int (input("enter the second number:"))

# quotient = num_1 // num_2
# reminder = num_1 % num_2

# print("the quotient is :", quotient , "and reminder is ", reminder)

# Q5  Write a program to enter P, T, R and calculate simple Interest & compound interest

# P = int(input("enter the principle amount:"))
# R = int(input("enter the rate of interest :"))
# T = int(input("enter the time period:"))

# sim_int = (P * R * T ) / 100

# A = P * (1 + R / 100 ) ** T
# comp_int = A - P

# print("Simple interest is ", sim_int)
# print("Compound interest is ", comp_int )


# Q6 Write a Program to input two angles from user and find third angle of the
# triangle.


# a1 = int (input("enter the first angle of triangle:"))
# a2 = int (input("enter the second angle of triangle:"))

# a3 = 180 - a1 -a2

# print("Third angle of triangle is :", a3)


# Q7 Program to Find the Roots of a Quadratic Equation


# a = int (input("enter the first variable:"))
# b = int (input("enter the second variable:"))
# c = int (input("enter the third variable:"))

# dis =  ((b * b ) - (4 * a * c)) ** 0.5


# root1 = (- b + dis ) / (2 * a) 
# root2 = (- b - dis ) / (2 * a)


# print("First root is ", root1 ,"second root is ", root2 )


# Q8 .Write a program to convert days into years, weeks and days.

# days= int (input("enter the days"))

# years = days // 365

# rem_days= days % 365 

# weeks= rem_days // 7

# days = rem_days % 7

# print(years ,"years",  weeks ,"week", days , "day")

# Q9. Write a program to enter base and height of a triangle and find its area.

# b = int(input("enter the base :"))
# h = int(input("enter the height:"))

# area = (b * h) / 2

# print("area of triangle is :", area)


# # Q10. Write a program to calculate area of an equilateral triangle.
# a = int(input("enter the side :"))

# area = ((3 ** 0.5 ) / 4) * a * a

# print("area of triangle is :", area)


# # Q11 .Find the area and circumference of circle.
# r = int (input("enter the radius of circle "))

# area_cir = 3.14 * r * r
# circum_cir = 2 * 3.14 * r

# print("area of circle is ", area_cir , "circumference of circle is ", circum_cir)

# Q 12 .Find the volume of sphere.

r = int (input("enter the radius of sphare : "))

vol = (4 / 3) * 3.14 * r * r * r

print("the volune of sphare is " , vol )
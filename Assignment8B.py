# 1. Write a program to calculate area of rectangle

# def area_react():

#     l = 5
#     b = 10 
    
#     area  = l * b

#     return area

# res = area_react()

# print(res)


# # 2. Write a program to calculate area of circle

# def area_circle():

#     r = 9

#     area = 3.14 * r * r


#     return area

# res = area_circle()

# print(res)



# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n

# def sum_series():
#     n = 10
#     sum = 0
#     for i in range(1 , n + 1):
            
#             sum = sum + i
    
#     return sum

# res = sum_series()

# print(res)

# b. 1!+ 2! + 3! + 4!+..... + n!


# def sum_series():

#     n = int(input("enter the number :"))
#     fact= 1
    
#     for i in range (1 , n + 1):
        
#          fact = fact * i 
    
#     return fact
    
# res = sum_series()

# print(res)


# c. 1^1 + 2^2 + 3^3+ ...... n^n
# def sum_series():
     
#         n = int(input("enter the number "))
#         sum =0

#         for i in range(1, n+1):

#             sum = sum  + (i ** i) 

#         return sum

# res = sum_series()

# print(res)



# 4. Sum of all odd numbers between 1 to n

# def sum_odd():

#     num = int(input("enter the number "))
#     sum = 0
#     for i in range (1 , num + 1):
#             if i % 2!= 0:
#                   sum = sum + i 
#     return sum
# res = sum_odd()    
# print(res)              

# 5. Sum of all prime numbers between 1 to n

# def sum_prime():
   
# n = int (input("enter the number :"))
# i = 2
# count =0 
# while count < 0:
#   for i in range(2, n):

#         if n % i == 0 :
#             break
#         else:
#          print(i)
#         count = count+1

#         n = n + 1
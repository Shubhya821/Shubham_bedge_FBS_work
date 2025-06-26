# 1. Write a program to calculate area of rectangle

# def area_rect():
      
#       l = 5
#       b = 4 

#       area = l * b

#       print("area of rectangle", area)
# area_rect()


# 2. Write a program to calculate area of circle

# def area_circle():
#       r = int(input("enter the redius"))

#       area=  3.14 * r * r

#       print("area of circle is ", area)
# area_circle()  

# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n


# def seriesa():

#         n = int(input("enter the number till sum you want :"))
#         sum = 0
#         for i in range(1, n+ 1):
#                 sum = sum  + i
#                 i = i + 1
#         print("the sum of series is ", sum)
# seriesa()


# b. 1!+ 2! + 3! + 4!+..... + n!


def sum_fact():
    n = 5 
    i = 1
    fact = 1
    for i in range(1, n+1):
          
          fact = fact * i
        #   i = i + 1
    print(" the sum is ", fact)

sum_fact()

# c. 1^1 + 2^2 + 3^3+ ...... n^n

# def power():
#     n = int(input("enter the number till you want "))

#     pwr = 0
#     for i in range(1 , n+ 1):

#         pwr = pwr + i ** i
        
        
#     print(pwr)
# power()


# 4. Sum of all odd numbers between 1 to n


def sum_odd():

    n = int(input("enter the number till wnat"))

    sum = 0
    
    for i in range(1 , n+1):

        if i % 2 != 0:
           
            sum = sum + i 
            
    print(sum)

sum_odd()

# # 5. Sum of all prime numbers between 1 to n

# def cal_prime():

#        n = int (input("enter the number till want: "))

#        i = 2
#        sum = 0

#        for i in range(2, n+1):
           
#             if i % 1 == 0:
                                                        # not completet
#                sum = sum + i

#        print(sum)

# cal_prime()

# 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms


# def fib_series():

#     n = int(input("enter the number till want "))
#     f = 1
#     s = 1                                                           not complete
#     t = 0 
        
#     for i in range(1, n + 1):
            
#             f = s
#             t = f + s
#             f , s = s , t

#             print(t)

# fib_series()



# 7. Write a program to find sum of digits of a number.


# def sum_dig():

    # num = int(input("enter the number"))
    # quo = num
    # sum = 0
    # while num != 0:
       
    #     quo = num % 10    
    #     num = num // 10
        
#         sum = sum + quo
        
#     print(sum)

# sum_dig()        


# 8. Write a program find reverse of a number

# def rev_num():
        
#     num = int(input("enter the number :"))

#     num = quo

#     while num != 0:
                    
#      quo = num % 10    
#      num = num // 10

#     print(num)

# rev_num()        


# 9. Write a program to check if entered number is a palindrome or
# not.

# def check_palidro():
        
#         n = int(input("enter the number :" ))
#         rev = 0 
#         temp = n 
#         while n > 0 :
#                 digi = n % 10 
#                 rev = rev * 10 + digi
#                 n = n //  10 


#         if temp == rev:
#             print("the number is palidrome")
#         else:
#                print("number is not palidrome")
# check_palidro()
            

# 10. Write a program to check if entered year is a leap year or not.

# def leap_year():

#     year = int(input("enter the year:"))


#     if year % 4 ==0:

#         if year % 400 != 0 or year % 100 ==0 :

#             print("year is leap")
#         else:   
#             print("year is not leap ")

#     else: 
#         print("year is not leap ")

# leap_year()



# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.  
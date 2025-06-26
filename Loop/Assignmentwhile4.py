# 1. WAP to print all even numbers until n.

# n = int (input("enter the number till you want :"))
# i = 1
# while i <= n:
#      if i % 2 == 0:
#           print(i)       
#      i = i + 1     


# 2. WAP to print all odd numbers until n.

# n = int(input("enter the number : "))

# i = 1

# while i <= n:
#      if i % 2 != 0:
#           print(i)
#      i = i + 1     

# 3. WAP to print sum of series upto n.

# n = int(input("enter the number :"))
# sum = 0
# i = 1

# while i <= n :
#     sum = sum + i
#     i = i + 1  

# print(sum)


# 4. WAP to print factorial of a number .

# n = int(input("enter the number :"))
# i = 1
# f = 1

# while i <= n:
#       f = f * i
#       i = i + 1

# print("the factorial of number is ", f ) 

# 5. WAP to print Fibonacci series upto n.

# n = int (input (" enter the number till you want"))
# i = 0
# f = 1

# while i <= n:
#      print(f)
#      i , f = f, i + f

#  6. WAP to check if a given number is prime number or not.   
# i = 2
# n = int(input("enter the number "))
# flag = True

# while i < n:
#       if n % i == 0:
#          flag = False
#          break
#       i = i + 1
# if flag == True:
#    print("number is prime")
# else:
#      print("number is not prime")




# 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.

# n = int(input("enter the number :"))
# i = 1

# while i <= n:
#       if i % 2 != 0 and i % 3 != 0 :
#          print( i )
#       i = i + 1


# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

# n = int(input("enter the numbers between till you want"))

# i = 1

# while i <= n:
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
    
# else: 
#     print("number is not avaialble ")


# 9. WAP to print all numbers in a range divisible by a given number.

# n = int(input("enter the number "))
# i = 1
# while i <= n:
#     if  i == n * i:
#         print(i)
        
#     i = i + 1
      
#  10. WAP to check if given number is Perfect Number.     

# num = int (input("enter the number :"))
# i = 1
# sum = 0

# while i < num:
#       if num % i == 0:
      
#           sum = sum + i 
 
#       i = i + 1

# if sum == num:
#     print("number is perfect")
# else:
#      print("num is not perfect ")


# 11. WAP to check if given number Strong Number.

# num = int (input("enter the number "))
# sum = 0
# quo = num

# while (quo != 0) :
#         d1 = quo % 10
#         quo = quo // 10 
        
#         i = 1
#         fact= 1
#         while i <= d1:
#                 fact = fact * i 
#                 i = i +  1
#         sum = sum + fact    
# if sum == num:
#         print("num is strong:")
# else:
#         print("num is not strong")


# 12. WAP to print Armstrong number within a given rang

# i = 100

# while i < 1000:
#       num = i
#       sum = 0

#       while num!=0:
            
#            rem = num % 10
#            num = num // 10
#            sum = sum + (rem ** 3)
#       if sum == i: 
#           print(i)      
#       i = i + 1
            
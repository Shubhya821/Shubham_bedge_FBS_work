# # Q1. To check number is positive or negative
# num = int(input("enter the number :"))

# if num > 0 :
#     print("number is positive ")
# else:
#     if num < 0:
#         print("number is negative")
#     else:
#         print("number is zero")


# Q2. input any alphabate that check it is vowel or consonant

# alp = input("Enter the alphabet: ")

# if alp == 'a' or alp == 'e' or alp == 'i' or alp == 'o' or alp == 'u' or \
#    alp == 'A' or alp == 'E' or alp == 'I' or alp == 'O' or alp == 'U':
#     print("Alphabet is a vowel!!")
# else:
#     print("Alphabet is a consonant!!")

# # Q3.input angle of triangle check weather triangle is valid or not 

# angle1 = int(input("enter first angle of triangle "))
# angle2 = int(input("enter second angle of triangle "))
# angle3 = int(input("enter third angle of triangle "))

# if angle1>0 and angle2>0 and angle3>0:
#     if angle1 + angle2 + angle3 == 180:
#       print("triangle is valid ")
#     else:
#       print("triangle is not valid ")
# else:
#    print("angle is not greater than zero so its invalid")


# # Q4. take all side of triangle and check weather triangle is valid or not 

# # # a= float (input("enter the first side of trianlge :"))
# # # b= float (input("enter the second side of trianlge :"))
# # # c= float (input("enter the third side of trianlge :"))

# # # if a > 0 and b > 0 and c > 0:
# # #     if a + b > c and b + c > a and a + c > b:
# # #            print ("triangle is valid !!")
# # #     else:
# # #            print("triangle is not valid ")
# # # else:
# # #      print("side is not greater than zero so its invalid !!")           



# Q5. check triangle is equilatral or isoscales , scalene triangle.

# s1 = int (input("enter the first side of triangle :"))
# s2 =int (input("enter the second side of triangle :"))
# s3 = int(input("enter the third side of triangle :"))

# if s1 == s2 and s2 == s3 and s1 == s3 :
#       print("triangle equilatrel ")
# elif s1 == s2 or s2 == s3 or s1 == s3:
#       print("triangle is isoscale")
# else:       
#       print("triangle is scalene")

# # # Q6.write a programe to calculate profit and loss


# # # cp = int (input("enter the cost price :"))
# # # sp = int (input("enter the selling price:"))

# # # if sp > cp:
# # #     profit = sp - cp
# # #     print("profit", profit)
# # # else:
# # #  if sp < cp:
# # #     loss = cp - sp     
# # #     print("loss", loss)
# # #  else:
# # #     print("no profit no loss")


# # # Q7. check if user enter the correct user id and  password 

# # # usr_id = input("enter the user id ")

# # # if usr_id == "ABC":
# # #        pwd = input("enter the password ")   
# # #        if pwd == "123":
# # #                print("login credinals are correct")
# # #        else: 
# # #              print("password is not correct")
# # # else:
# # #    print("invalid user name")        


# # # Q8.write a pro to promt user to enter userid and password after verigying
# # # userid and password display 4 digit random number and ask user to enter the Same
# # # if user enter the same number then show him sucess massage other failed (something like captcha)


# # use_id = input("enter the userid :")

# # if use_id == "abc":
# # #     pwd = input("enter the password")
# # #     if pwd == "123":
      
# # #     #  print("login successful")
# # #     else:
# # #        print("invalid password")
# # # else:
# # #    print("incorrect user id ")       


# # # Q9. input 5 subject marks from user and display grade (eg first class second class)

# # mark1 = float (input("enter the marks of sub 1 "))
# # # mark2 = float (input("enter the marks of sub 2 "))
# # # mark3 = float (input("enter the marks of sub 3 "))
# # # mark4 = float (input("enter the marks of sub 4 "))
# # # mark5 = float (input("enter the marks of sub 5 "))

# # # total_marks = mark1 + mark2 + mark3 + mark4 + mark5

# # total_per = (total_marks / 500) * 100  

# # if total_per >= 90:
# #     print("student passed with fist class", total_per)
# # else:
# #     if total_per >= 70 and total_per <= 89:
# #      print("student passed with second class", total_per)
# #     else:
# #      if total_per >= 50 and total_per <= 69:
# #         print("student passed with third class", total_per)
# #      else:
# #         print("student just passed ", total_per)



# # Q10. write a programe to check if person is eligible to marry or not (male age> = 21 and female age > = 18)

# male_age = int (input("enter the male age:") )
# if male_age >= 21:
#     print("male eligible to marry")
# else: 
#     print("male is not eligible ")         
# female_age = int (input("enter the female age:") )

# if female_age >= 18:
#         print("female is eligible")
# else:
#          print("female is not eligible to marry ")


# male_age = int(input("Enter the male age: "))
# female_age = int(input("Enter the female age: "))

# if male_age >= 21:
#     print("Male is eligible to marry.")
# else:
#     print("Male is not eligible to marry.")

# if female_age >= 18:
#     print("Female is eligible to marry.")
# else:
#     print("Female is not eligible to marry.")


# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

# age1 = int(input("enter the age of first person"))
# tic1 = int(input("enter the ticket amount of first person"))

# age2 = int(input("enter the age of 2nd person"))
# tic2 = int(input("enter the ticket amount of 2nd person"))

# age3 = int(input("enter the age of 3rd person"))
# tic3 = int(input("enter the ticket amount of 3rd person"))

# age4 = int(input("enter the age of 4th person"))
# tic4 = int(input("enter the ticket amount of 4th person"))

# age5 = int(input("enter the age of 5th person"))
# tic5 = int(input("enter the ticket amount of 5th person"))

# if age1 < 12:
#  tic1 = tic1 - tic1 * 0.30
# elif age1 > 59:
#  tic1 = tic1 - tic1 * 0.50

# if age2 < 12:
#  tic2 = tic2 - tic2 * 0.30
# elif age2 > 59:
#  tic2 = tic2 - tic2 * 0.50 

# if age3 < 12:
#  tic3 = tic3 - tic3 * 0.30
# elif age3 > 59:
#  tic3 = tic3 - tic3 * 0.50

# if age4 < 12:
#  tic4 = tic4 - tic4 * 0.30
# elif age4 > 59:
#  tic4 = tic4 - tic4 * 0.50

# if age5 < 12:
#  tic5 = tic5 - tic5 * 0.30
# elif age5 > 59:
#  tic5 = tic5 - tic5 * 0.50  

# total_amount = tic1 + tic2 + tic3 + tic4 + tic5
# print("total amount of ticket is ",total_amount)


# 12. Write a program to check if given 3 digit number is a palindrome or not.

# num = int(input("enter the three digit number "))

# r1 = num % 10 
# quo = num // 10 

# r2 =  quo % 10 
# r3 = quo // 10 

# if r1 == r3 and r2 == r2:
#     print("number is palidrome")
# else:
#     print("number is not palidrome") 



# 13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill



# units = int(input("enter the units:"))

# if units <= 50:
#     bill = units * 0.50
# elif units <= 150:
#     bill = (50 * 0.50) + ((units - 50) * 0.75)
# elif units <= 250:
#     bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
# else:
#     bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

# surcharge = bill * 0.20
# total_bill = bill + surcharge

# print("Total electricity bill is Rs.", total_bill)

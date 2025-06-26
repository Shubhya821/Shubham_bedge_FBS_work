# sub1=100
# sub2=20
# sub3=100
# sub4=50
# sub5=30

# total=sub1+sub2+sub3+sub4+sub5

# per= (total/500) * 100
# print(per)


# a= 10 
# b = 20

# a = a + b
# b= a - b
# a = a - b
# print(a , b)

# Input: a 3-digit number
num = int(input("Enter a 3-digit number: "))

# Extract digits
digit1 = num % 10
num = num // 10

digit2 = num % 10
num = num // 10

digit3 = num

# Calculate reverse
reverse = (digit1 * 100) + (digit2 * 10) + digit3

# Output the result
print("Reversed number is:", reverse)

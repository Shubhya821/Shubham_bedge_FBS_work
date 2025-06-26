# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total = 0 
i = 1

while i <= 5:
    age = int(input("enter the age"))
    tic = int(input("enter the ticket amount"))

    if age <= 12:
       tic = tic * 0.7
    elif age >= 59:
        tic = tic * 0.5

    total = total + tic
    i = i + 1

print(total)
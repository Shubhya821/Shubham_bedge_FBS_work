i = 100

while i < 1000:
   
    num = i 
    sum = 0
    
    while num!=0:
        rem= num % 10
        num = num //10
        sum = sum + (rem**3)

    if sum == i:
        print(i)
    i = i + 1    
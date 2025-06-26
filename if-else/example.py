num = int(input("Enter the three digit: "))

dig_1 = num % 10         # Units place
quo = num // 10

dig_2 = quo % 10         # Tens place
dig_3 = quo // 10        # Hundreds place

if dig_1 == dig_2 * 2 and dig_1 == dig_3 / 2:
    print("Yes, you have done it!")
else:
    print("try next time")

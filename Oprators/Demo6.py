days= int (input("enter the days"))

years = days // 365

rem_days= days % 365 

weeks= rem_days // 7

days = rem_days % 7

print(years ,"years",  weeks ,"week", days , "day")
year = int(input("Enter a year: "))

divid_4 = year % 4
divid_100 = year % 100
divid_400 = year % 400

if divid_4 != 0:
  print(f"{year} is not a leap year.")
elif divid_100 == 0:
   if divid_400 != 0:
      print(f"{year} is not a leap year.")
   else:
      print(f"{year} is a leap year.")
else:         
   print(f"{year} is a leap year.")


# 2)  if-else + AND & OR 
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
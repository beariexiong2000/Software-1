calculator = input("Choose the calculator (add, minus, multiplication, division): ")
import math
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if calculator == "add":
  result = num1 + num2
  print (result)
elif calculator  == "minus":
  result = num1 - num2 
  print (result)
elif calculator == "multiplication":
  result = num1 * num2
  print (result) 
elif calculator == "division":
  while num2 == 0:
    result = "Error: Dividing by 0 is not allowed! Please enter again" 
    print (result)
    num2 = float(input("Enter the second number: "))
  if num2 != 0:
    result = num1 / num2
  print (result)
else:
  result = "Invalid calculator choice. Please choose numbers again"
  print (result)
  print (calculator)

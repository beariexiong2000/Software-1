import random

code_3digit = ""
while len(code_3digit) < 3:
  num = random.randint(0,9)
  code_3digit += str(num)

code_4digit = ""
while len(code_4digit) < 4:
  num = random.randint(1,6)
  code_4digit += str(num)

print("3-digit code: " + code_3digit)
print("4-digit code: " + code_4digit) 
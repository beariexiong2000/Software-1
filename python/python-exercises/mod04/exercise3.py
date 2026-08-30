BG =input("Enter biological gender (male/female): ")

HV =float(input("Enter hemoglobin value (g/l): "))
if BG.lower() == "male":
   if HV < 134:
     print("Your hemoglobin is low.")
   elif HV > 167:
     print("Your hemoglobin is high.")
   else:
     print("Your hemoglobin is normal.")
elif BG.lower() == "female":
   if HV < 117:
     print("Your hemoglobin is low.")
   elif HV > 155:
     print("Your hemoglobin is high.")
   else:
     print("Your hemoglobin is normal.")

else:
  print("Invalid gender.")
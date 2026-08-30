zander_size = float(input("Enter the length of the zander in centimeters: "))
if zander_size >= 42:
    print("The zander meets the size limit.")
else:
    missing_size = 42 - zander_size
    print("Please release the fish back into the lake.")
    print(f"The fish was {missing_size:.1f} centimeters below the size limit.")
    
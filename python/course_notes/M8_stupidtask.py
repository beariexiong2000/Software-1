# 这是一个很愚蠢的作业，完全无法理解出卷人想要我干什么，这个脱离实际应用的任务。看不懂
print("") #奇怪的细节，一行是空白的

print("Airport Data Management")
print("1. Enter a new airport")
print("2. Fetch airport information")
print("3. Quit")

option = input("Please choose an option (1-3): ")

# 设一个空的dictionary
airports = {} 

# 进入重复环节
while option != "3":
    if option == "1":
      
        icao = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")
        # store the new airport to dictionary
        airports[icao] = name

        print(f"Airport {name} with ICAO code {icao} has been added.")
    elif option == "2":
        # fetch information from dictionary
        icao = input("Enter the ICAO code: ")

        # get airport information from the dictionary and print it
        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}.")
        else:
            print(f"No airport found with ICAO code {icao}.")

    print("")

    print("Airport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    # in these kind of assignments / situations the while loop usually ends with input
    # the while condition "option != "3"" will check should we continue to next line
    option = input("Please choose an option (1-3): ")


print("Thank you for using the Airport Data Management system. Goodbye!")
start = int(input("Enter 1 to start your budget planner. Enter any other number to exit.: ")) # User enters 1 to start to budget planner.
while start == 1:   # Budget planner runs while start is 1.
    print("Welcome to your monthly Budget Planner!")     # Welcomes the user to the budget planner.
    name = (input("Enter your name here: "))     # Asks the user for their name.
    monthlyRent = float(input("Enter your monthly rent here: "))  # Asks the user for their monthly rent.
    monthlyInternet = float(input("Enter your monthly internet bill here: ")) # Asks the user for their monthly internet bill.
    monthlyGrocery = float(input("Enter your monthly grocery bill here: "))  # Asks the user for their monthly grocery bill.
    monthlyFun = float(input("Enter your monthly fun allowance here: "))  # Asks the user for their monthly "fun" allowance.
    monthlyExpenses = float(monthlyRent + monthlyInternet + monthlyGrocery + monthlyFun)  # Gives the total of all monthly expenses.
    hourlyWage = float(10)     # Variable for the hourly wage
    hoursWorked = float(1)     # Variable for the hours worked
    pay = hourlyWage * hoursWorked    # Multiplies hours worked by hourly wage to calculate pay.
  
    while pay < monthlyExpenses:      # Function to keep increasing the hours worked by one hour.
        hoursWorked = hoursWorked + 1
        pay = hourlyWage * hoursWorked
   
    # Variables below are to ensure accuracy for any numbers that are not multiples of 10)
        excessPay = pay - monthlyExpenses   # Takes any excess pay from the funtion.
        pay = pay - excessPay   # Subtracts any excess pay to that the pay can equal the correct amount.
        hoursWorked = pay / 10   # Divides pay by 10 to get an exact amount for hours worked.
        
        print(name)       # Prints the user's name.
        print(f"Your hourly wage is ${hourlyWage}")          # Prints the user's hourly wage.
        print(f"Your monthly rent is ${monthlyRent}")        # Prints the user's monthly rent.
        print(f"Your monthly internet bill is ${monthlyInternet}")    # Prints the user's monthly internet bill.
        print(f"Your monthly grocery bill is ${monthlyGrocery}")      # Prints the user's monthly grocery bill.
        print(f"Your monthly fun allowance is ${monthlyFun}")         # Prints the users fun allowance.
        print(f"The total of your monthly expenses is ${monthlyExpenses}")    # Prints the users monthly expenses
        print(f"You need to work {hoursWorked} hours and make ${pay} to break even.")   #Prints how many hours the user has to work in order to break even
        print(f"You need to work {hoursWorked + 10} hours to make ${pay + 100} for $100 in monthly savings")     # Prints how many hours the user has to work in order to make $100 in savings.
        start = int(input("Enter 1 to continue using your budget planner. Enter any other number to exit.:"))    # User has to enter 1 again to continue using the budget planner or enter any other number to exit.
    
print("Thank you for using your monthly budget planner. Goodbye!! :)")      # Ends the budget planner.



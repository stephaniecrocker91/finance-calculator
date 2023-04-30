import math

# PROGRAM REQUESTS USER TO TYPE MENU OPTION: 'investment' or 'bond'

print("\ninvestment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan\n")

# Option input is lowercased to avoid case-sensitivity errors.
option = (input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()
print(option)


# CONDITIONAL STATEMENT DEPENDING ON USER INPUT

# If user inputs nothing or input doesn't match options...
if option == "":
    print("No option selected. Please try again.\n")
elif option != "investment" and option != "bond":
    print("You selected an invalid option.\n")

# -------------------------------------------------------------------------------------
# If user inputs 'investment'...
elif option == "investment":
    print("\n_________________________\n\nYou selected 'INVESTMENT'\n_________________________\n")
    # Input requests to collect investment info for calculations and convert to float.
    money = float(input("\nPlease enter the amount you wish to deposit: \n"))
    # Interest rate value is divided by 100 and stored. (To facilitate later calculations)
    rate = float(input("\nPlease enter the interest rate as a %.\nDon't worry about including the % sign \n"))/100
    years = float(input("\nPlease enter the number of years you plan on investing: \n"))
    interest = (input("\nPlease select interest type: 'simple' or 'compound': \n")).lower()

    # Conditional statment depending on user 'interest' input
    # If user inputs nothing or input doesn't match...
    if interest == "":
        print("No option selected. Please start this process again.\n")
    elif interest != "simple" and interest != "compound":
        print("You selected an invalid option. Please start this process again.\n")
    # simple interest formula and results
    elif interest == "simple":
        print("\n______________________________\n\nYou selected 'SIMPLE' interest\n______________________________\n")   
        total = money * (1 + rate * years)
        print("Your total amount = {}\n".format(total))
    # compound interest formula and results
    else:
        print("\n_________________________________\n\nYou selected 'COMPOUND' interest\n_________________________________\n")
        total = money * math.pow((1 + rate), years)
        print("Your total amount = {}\n".format(total))


# -------------------------------------------------------------------------------------
# If user inputs 'bond'...
else:
    print("\nYou selected 'BOND'\n_________________________\n")
    # Input requests to collect bond info for calculations and convert to float.
    value = float(input("\nPlease enter the value of the house: \n"))
    # Interest rate value is divided by 100, then by 12 and stored. (To facilitate later calculations)
    rate = float(input("\nPlease enter the interest rate as a %.\nDon't worry about including the % sign \n"))/100/12
    months = float(input("\nPlease enter the number of months you plan to take to repay the bond: \n"))
    
    total = (rate * value)/ (1 - (1 + rate) ** (-months))
    print("\nYour total bond repayment = {}\n".format(total))
    

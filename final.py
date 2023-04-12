"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""
c = 0


def coin_Calc(c, quarter, dime, nickel, penny):
    """This method calculates the amount of coins provided by the user and divides 
    them by quarters, dimes, nickel, and pennies. 
    @param c this is the users coin input
    @param quarter this provides the user the quarters outcome change 
    @param dime this provides the user the dime outcome change
    @param nickel this provides the user the nickel outcome change
    @param penny this provides the user the penny outcome change
    """
    if c >= 0:
        """This if statement sets the varible that is greater than or equal to zero
        to run the floor division of quarters, dimes, nickel, pennies. 
        """
        if c >= 25:
            """This if statement 
            """
            quarter = c // 25
            c = c - 25 * quarter
            penny = c 
        elif c >= 10:
            dime = c // 10
            c = c - 10 * dime
            penny = c 
        elif c >= 5:
            nickel = c //5
            c = c - 5 * nickel
            penny = c 
        else:
            penny = c 
    else:
        c = 0
    return quarter, dime, nickel, penny
      
      
def main():
    user = "y"
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    print("Coin Return Calculator")

    while user.lower() == "y": 
        noErr = False
        while noErr == False:
            try:
                c = int(input(f"\nEnter change amount to convert: "))

                if c <= 0:
                    raise ValueError("Error! Invalid interger entered please try again.")

                q, d, n, p = coin_Calc(c, quarter, dime, nickel, penny)
        
                print(f'{q} quarter(s)')
                print(f'{d} dime(s)')
                print(f'{n} nickel(s)')
                print(f'{p} penny(ies)')

        
                noErr = True

                if c <= 0:
                    raise ValueError ("Error! Invalid interger entered please try again.")

                

            except:
                print ("Error! Invalid interger entered please try again.")

        user = input (f"Want to calculate another amount? (y/n): ")

    print(f"\nBye, have a good day and don't drop out!")

if __name__ == "__main__":
    main()
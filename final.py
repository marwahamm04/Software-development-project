"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""
c = 0


def coin_Calc(c, quarter, dime, nickle, penny):
    """This method calculates the amount of coins provided by the user and divides 
    them by quarters, dimes, nickles, and pennies. 
    @param c this is the users coin input
    @param quarter this provides the user the quarters outcome change 
    @param dime this provides the user the dime outcome change
    @param nickle this provides the user the nickle outcome change
    @param penny this provides the user the penny outcome change
    """
    if c >= 0:
        """This if statement sets the varible that is greater than zero
        to run the floor division of quarters, dimes, nickles, pennies. 
        """
        if c >= 25:
            quarter = c // 25
            c = c - 25 * quarter
        if c >= 10:
            dime = c // 10
            c = c - 10 * dime
        if c >= 5:
            nickle = c //5
            c = c - 5 * nickle
        else:
            penny = c // 1
    else:
        c = 0
    return quarter, dime, nickle, penny
      
      

def main():
    user = "y"
    quarter = 0
    dime = 0
    nickle = 0
    penny = 0

    print("Coin Return Calculator")

    while user.lower() == "y": 
        noErr = False
        while noErr == False:
            try:
                c = int(input(f"\nEnter change amount to convert: "))

                if c <= 0:
                    raise ValueError("Error! Invalid interger entered please try again.")

                q, d, n, p = coin_Calc(c, quarter, dime, nickle, penny)
        
                print(f'{q} quarter(s)')
                print(f'{d} dime(s)')
                print(f'{n} nickle(s)')
                print(f'{p} penny(ies)')

        
                noErr = True

                

            except:
                print ("Error! Invalid interger entered please try again.")

        user = input (f"Want to calculate another amount? (y/n): ")

    print(f"\nBye!")

if __name__ == "__main__":
    main()

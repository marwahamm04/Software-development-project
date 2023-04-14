"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""
c = 0


def coin_Calc(c, quarter, dime, nickel, penny):
    
    if c >= 0:
        if c >= 25:

            quarter = c // 25
            c = c - 25 * quarter
            penny = c 
        elif c >= 10:
            dime = c // 10
            c = c - 10 * dime
            penny = c 
        elif c >= 5:
            nickel = c // 5
            c = c - 5 * nickel
            penny = c 
        else:
            penny = c 
    else:
        c = 0
    return quarter, dime, nickel, penny
      
      
def main():
    """! The main class. This is where the input, print, while and if statements are located,
    along with the initialization of variables and the closing statement.
    @author Justin Wareham
    """
    user = "y"
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    print("Coin Return Calculator")

    while user.lower() == "y":
        """ This while loop uses the user input (y/n) to decide whether to continue using the 
            calculator or to print the closing statement.
            @author Justin Wareham
        """
        noErr = False
        while noErr == False:
            """ This while loop prints out a question asking the user if they would like to attempt
                the calculator again as long as the answer is the letter y.
                @author Justin Wareham
            """
            try:
                """ This try loop asks for the input of change the user wants converted.
                    @author Justin Wareham
                """
                c = int(input(f"\nEnter change amount to convert: "))

                if c <= 0:
                    raise ValueError("Error! Invalid integer entered please try again.")

                q, d, n, p = coin_Calc(c, quarter, dime, nickel, penny)
        
                print(f'{q} quarter(s)')
                print(f'{d} dime(s)')
                print(f'{n} nickel(s)')
                print(f'{p} penny(ies)')

        
                noErr = True

                if c <= 0:
                    raise ValueError ("Error! Invalid integer entered please try again.")

                

            except:
                print ("Error! Invalid integer entered please try again.")

        user = input (f"Want to calculate another amount? (y/n): ")

    print(f"\nBye, have a good day and don't drop out!")


if __name__ == "__main__":
    main()
    """ This calls the main function.
    @author Justin Wareham
    """
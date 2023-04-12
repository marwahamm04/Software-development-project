"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""
c = 0


def coin_Calc(c):

    quarters = c // 25
    c = c % 25

    dimes = c // 10
    c = c % 10

    nickels = c // 5
    c = c % 5

    pennies = c

    return [quarters, dimes, nickels, pennies]
      

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
                noErr = True

                if c <= 0:
                    raise ValueError("Error! Invalid Integer entered please try again.")

                q, d, n, p = coin_Calc(c, quarter, dime, nickel, penny)
        
                print(f'{q} quarter(s)')
                print(f'{d} dime(s)')
                print(f'{n} nickel(s)')
                print(f'{p} penny(ies)')

        

                

            except:
                print ("Error! Invalid interger entered please try again.")

        user = input (f"Want to calculate another amount? (y/n): ")

    print(f"\nBye, have a good day and don't drop out!")

if __name__ == "__main__":
    main()

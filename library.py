from string_utils import is_number

letter = False

if letter == False:
    
    c = input("\n Enter your coin amount = ")
 
    if is_number(c) == True:
        print("good job!")
    else:
        raise ValueError("This is not an number")
        
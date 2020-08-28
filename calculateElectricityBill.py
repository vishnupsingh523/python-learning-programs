# defining main function here:
def main():
    print("****  WELCOME TO THE ELECTRICITY BILL CALCULATOR  ****\n")
    
    units = int(input("Enter the number of units: "))
#     calling the function calculateBill with the parameter units:
    
    rateOfCharge = 0
    if units>=0:
        if units <= 150:
            rateOfCharge = units*3
        elif units<=350:
            rateOfCharge = 100 + units*(3.75)
        elif units<=450:
            rateOfCharge = 250 + units*4
        elif units<=600:
            rateOfCharge = 300 + units*(4.25)
        elif units > 600:
            rateOfCharge = 400 + units*5
            
#     printing the amount of money
    print("Total amount:  Rs.",rateOfCharge)
    
main()

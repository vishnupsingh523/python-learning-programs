# in this program we are checking weather the car name entered by user is present in the dictonary or not
# if it is prsent then simply print "Yes, its present" othrwise take the iput for price then print the whole list


CarsName={"Audi":1600000,"Mercedes Benz":3600000,"Lamborghini":2600000,"BMW":1700000}
CarsName_items=CarsName.items()
# sorting the dictionary
sorted_items=sorted(CarsName_items)

print("Here is the sorted list of CARS: ",sorted_items)

# taking the input form the user 
CarName=input("\nEnter the car name which you want: ")

count = 0

for key in CarsName.keys():
    if CarName == key:
        print("\nYes, the car is present")
        count = 0
        break
    else:
        count = count + 1

#         checking and printing the dictionary
if count >0:
    Price = int(input("\n Enter the price: "))
    CarsName[CarName] = Price
    
    print("Final CarsList: ",CarsName)

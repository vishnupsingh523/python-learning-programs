# this program is to find the greatest of three numbers:
def maxofThree():
#   taking the input of three numbers
    x = int(input("A : "));
    y = int(input("B : "));
    z = int(input("C : "));
    
   #performing the conditions here for finding the greatest
    if x>y:
        if x>z:
            print(x," is the greatest")
        else:
            print(z," is the greatest")
    elif y>z:
        print(y, " is the greatest")
    else:
        print(z, " is the gretest")
        
# calling the maxofThree function here:
maxofThree()

from circumference import calculate_circumference
from squarefootage import square_footage
from shoppingcart import shopping_cart

#Excercise 1
shopping_cart()

#Exercise 2
# get user's input
done = False
while not done:
    users_choice = input("Do you want to calculate circle's circumference(cc) or house square footage(sf)? ").lower()
    if(users_choice == "cc"):
        radius = float(input("Enter radius for circle: "))
        print(calculate_circumference(radius))
    elif(users_choice == "sf"):
        width = float(input("Enter width in feet: "))
        height = float(input("Enter height in feet: "))
        print(square_footage(height, width))
    else:
        input("Invalid!! Press any button to continue. ")
        continue
    
    confirm = input("Do you want to continue(Y/N)? ").lower()
    if(confirm == 'y'):
        done = False
    else:
        done = True

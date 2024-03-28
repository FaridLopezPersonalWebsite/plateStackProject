#Plate Stacking Project
#Create an empty list to hold plates for adding, removing or print
#AT THE END : Create a master function to CALL ALL the below functions and start the program
    #Print menu options
    # Deploy Exit in the stacking project function
        # User is able to exit 
        # Print Goodbye! Message when selected and program is over
#Create function Add a Plate 
    # Check for positive integer input
        #If zero is inputted print warning and dont append plate list:
        # If new plate inputted is larger than the plate below it:
            #Print warning and dont add plate
        # Else if plate is equal to or smaller than plate below it:
            #Append list and add plate 
# Create function Remove a plate 
    # User is able to remove a number of plates from top of stack
        # Positive integers only
            #Else if not positive print warning and don't remove plates
        # Number can't be less than or equal to zero
            #If zero is given :
                #print a warning
        #If there are too many plates selected:
            #Print a warning
        # If there are zero plates left :
            # print zero plates left
#Create function Print Plates
    #Stack plates vertically, largest to smallest
        #Order from largest at the bottom to smallest at the top
    #If no plates:
        #print message: No Plates Stacked!


#Create a List

plates = []

# Function to account for other user errors
def user_error(prompt): 
    value = ''
    while not value :
        value = input(prompt).strip()
        if not value :
            print('Error. Please input valid value.')
        return value

# Function to add plates
def add_plate():
    global plates
    add_plates = int(input('Enter the size of the plate:'))
    if add_plates <=0:
        print ('Error, plate choice is not valid, please try again.')
    elif not plates:
        plates.append(add_plates)
        print ('Success! Plate added')
    elif add_plates>plates[-1]:
        print('Error, the plate must be smaller than the plates below it, try again!')
    else:
        plates.append(add_plates)
        print ('Success! Plate added')

#Function to remove plates
def remove_plate():
    global plates
    remove_plates = int(input('Enter the plates you want to remove:'))
    if remove_plates <= 0:
        print ('Error, please enter a valid number')
    elif remove_plates > len(plates):
        print ( f'Error, cannot remove more than {plates.index()} plates. You entered {remove_plates}')
    else :
        plates.pop()
        print('Success! Plate(s) removed.')

#Function to print plates
def print_plates():
    for plate in reversed(plates):
        print('#'*plate)
    if plates == []:
        print('There are currently no plates, please add a plate.')

# Function to run the program 
def plate_stacker() :
    print('Welcome to Plate Stacker!') #Intro
    print('-'*25) #For display purposes 
    option = ''

    while option!= '0':
        print ('0. Exit')
        print('1. Add a Plate')
        print('2. Remove a Plate')
        print('3. Display Plates')
        option =user_error('Select [0-3]: ')
        if option == '0':
            print('Goodbye!')
        elif option == '1': 
            add_plate()
        elif option == '2':
            remove_plate()
        elif option == '3':
            print_plates()
        # else :
        #     print('I dont understand that command')

#Call function
plate_stacker()
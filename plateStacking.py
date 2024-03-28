#Plate Stacking Project
#Add a Plate 
    #Every new plate that is added must be <= the previous plate size, 
        # ie 9 cant be added on top of an 8 plate but 7 can.
        # Give error when user tries doing something like the above
    # While the plates are added, the list of plates is printed 
# Remove a plate 
    # User is able to remove a number of plates available
        # You can't remove 3 plates if only 2 are available
        # Error is given if the above is tried
        # If there are zero plates left then print zero plates left
# Exit 
    # User is able to exit 
    # Print Goodbye! Message when selected

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
def add_plate ():
    add_plates = input('What size plate do you want to add ? [0-10]: ')
    plates.append(f'{add_plates} is the number of plates now')
    print('Add a Plate')
    print(add_plates)

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
            print ('Remove a Plate')
        elif option == '3':
            print (*plates, sep = "\n")
        # else :
        #     print('I dont understand that command')

plate_stacker()
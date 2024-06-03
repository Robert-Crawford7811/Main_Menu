"""Menu system to create passwords and Math"""
import datetime
import math
import secrets
import string

def calc_decimal():
    '''Calculates and formats percentages'''
     # Prompt user for what numbers they are using for their decimal
    num = float(input('Enter an numerator: '))
    den = float(input('Enter an denominator: '))
    dec_points = int(input('Enter the number of decimal points: '))

    #Calculates the percentage the fraction evaluates
    result = round((num / den) * 100, dec_points)
    print("The percentage is", result,'%')

def calc_remaining_days():
    '''Function that calculates the remaining days until July 4th, 2025'''
    # Takes the current date
    today = datetime.date.today()
    # Establishes the reference date
    ref_day = datetime.date(2025, 7, 4)
    # Calculates the day remaining until the reference date
    remaining_days = ref_day - today
    # Prints the days remaining
    print("Remaining days until 07/04/2025: ", remaining_days)
def vol_cylinder():
    '''Function that calculates the volume of a right circular cylinder'''
    #Prompt user for dimensions of the cylinder
    r = float(input('What is the radius of your cylinder? '))
    h = float(input('What is the height of your cylinder? '))

    #Calculates the volume of cylinder
    vol = math.pi*(r**2)*h
    print("The volume of your cylinder is ", vol)

def triangle_leg():
    '''Function called to calculate leg c of an triangle'''
    #Prompts the user for the dimensions of the triangle
    a = int(input("What is the length of leg a of your triangle: "))
    b = int(input("What is the length of leg b of your triangle: "))
    angle_c = int(input("What is the angle measure c of your triangle: "))
    #Calculates leg c of the triangle
    c = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(angle_c)))
    print("Leg C of your triangle is equal to: ", c)

def generate_password():
    '''Function that generates a password within the parameters of the password'''
    #Input the parameters of the password
    length = int(input('Enter the length of the password: '))
    u_case = input('Do you want to use uppercase letters (Y/N): ')
    l_case = input('Do you want to use lowercase letters (Y/N): ')
    numbers = input('Do you want to use numbers (Y/N): ')
    special_char = input('Do you want to use special character (Y/N): ')
    complex_char = [u_case, l_case, numbers, special_char, length]
    upper_case = string.ascii_uppercase
    numbers = string.digits
    lower_case = string.ascii_lowercase
    special_characters = '!@#$%^&*()_-+={}[]\\|:;<>,.?/~'
    complex_list = []
    if complex_char[0] == 'y':
        complex_list.extend(list(upper_case))
    if complex_char[1] == 'y':
        complex_list.extend(list(lower_case))
    if complex_char[2] == 'y':
        complex_list.extend(list(numbers))
    if complex_char[3] == 'y':
        complex_list.extend(list(special_characters))
    password = ''.join([secrets.choice(complex_list) for _ in range(length)])
    print("Your password is ", password)

print("Select what you would like to accomplish!")
#Presents the options the user can choose from
print("1: Generate a Secure Password")
print("2: Calculate and Format a percentage")
print("3: How many days until July 4, 2025?")
print("4: Calculate the leg of an triangle")
print("5: Calculate the volume of a right circular cylinder")
print("6: Exit the program.")

# Menu System that allows user to select an operation
MENU_CHOICE = 0
#If the user hasn't ended the program they will be prompted for a decision
while MENU_CHOICE != 6:
    #Requests a decision to be made by the user
    MENU_CHOICE = int(input("What would you like to do: "))
    if MENU_CHOICE == 1:
        print("You are generating a password.")
        #Call the function that generates a password
        generate_password()
    elif MENU_CHOICE == 2:
        print("You are calculating a percentage")
        #Call the function to calculate and format decimal
        calc_decimal()
    elif MENU_CHOICE == 3:
        print("You are finding how many days until July 4, 2025")
        #Call function to calculate how long until July 4, 2025
        calc_remaining_days()
    elif MENU_CHOICE == 4:
        print("You are calculating the leg of an triangle.")
        #Call function to calculate the leg of a triangle using law of cosine
        triangle_leg()
    elif MENU_CHOICE == 5:
        print("You are calculating the volume of a cylinder")
        #Call function to calculate the volume of a right cylinder
        vol_cylinder()
    elif MENU_CHOICE == 6:
        print("Thank you for using the program")
        #Ends the program if selection 6 is chosen
        break
    else:
        #Prompts the user to attempt to make a correct selection
        print("Please Try Again.")

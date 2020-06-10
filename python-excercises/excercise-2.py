#Conditional Statements and example for if condition
age = 99
if age >= 35:
    print("You are old")
elif age >=30:
    print("You are becoming old")
elif age >= 25:
    print("You are not old enough to be a representatve")

print("Have a nice day!")

#Defining Functions
def say_hi():
    print('Hi!')

#Calling Functions
say_hi()

#Parameterized function example
def say_hi(name):
    print('Hi {}!'.format(name))

say_hi('Jason') #Output is: Hi Jason!
say_hi('everybody!') # Output is: Hi everybody!

#Function with optional parameter-Setting a default value
def say_hi(name = 'there'):
    print('Hi {}!'.format(name))

say_hi() # Hi there!
say_hi('Jason') # Hi Jason!

#Parameterized Functions with non-specific order
def say_hi(first,last):
    print('Hi {} {}!'.format(first,last))

say_hi(first = 'Jane', last='Doe') # Hi Jane Doe!
say_hi(last='Doe',first='John') # Hi Jane Doe!

#Required and optional parameters
def say_hi(first, last='Doe'):
    print('Hi {} {}!'.format(first,last))

say_hi('Jane') # Hi Jane Doe!
say_hi('John','Coltrane') # Hi John Coltrane

# Function definition,details and help function
def say_hi(first, last='Doe'):
    """Say hello."""
    print ('Hi {} {}!'.format(first,last))

help(say_hi) # press q to quit the help screen/mode

#Function with conditional return 
def odd_or_even(number):
    """Determine if a number is odd or even."""
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

odd_or_even_string = odd_or_even(7)
print(odd_or_even_string)  # Output is: Odd
print(odd_or_even(7))

#Function invoking other functions
def get_name():
    name = input('What is your name? ')
    return name

def say_name(name):
    print('Your name is {}.'.format(name))

def get_and_say_name():
    """Get and display name"""
    name = get_name()
    say_name(name)

get_and_say_name()
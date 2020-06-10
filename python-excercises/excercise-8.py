# Modules

#Importing all functions/methods from a package
import time
print(time.timezone)
print(time.asctime())

#Importing specific functions/methods from a package
from time import asctime
print(asctime())

#Importing multiple functions/methods from a package 
from time import asctime, sleep
print(asctime())
sleep(1)
print(asctime())

#Viewing all methods within a module/package
import time
print(dir(time))

#Search path for modules
import sys;
for path in sys.path:
    print(path)

#Manipulating search path
import sys;
sys.path.append('/Users/bharatuday/Desktop')
for path in sys.path:
    print(path)

#Programatically terminate a program
import sys
file_name = './File.txt'
try:
    with open(file_name) as test_file:
        for line in test_file:
            print(line.rstrip())
except:
    print("could not open file {}".format(file_name))
    sys.exit(1)


#Custom Package
#say_hi package
def say_hi():
    print('Hi!')

# Importing into another file
import say_hi
say_hi.say_hi() # Output: Hi!


#Example 2 for custom package
#When we import a package its code gets executed first
#File 1:
def say_hi():
    print('Hi!')

print('Hello from say_hi2.py!')

#File 2:
import say_hi2
say_hi2.say_hi() # Output is: Hello from say_hi2.py
                 # Hi!

#Controlling the execution of the program 
def say_hi():
    print('Hi!')

def main():
    print('Hello from say_hi3.py!')
    say_hi()

if __name__ == '__main__':  #__name__ is a built in variable.If the modules is imported then the main  function never gets executed.
    main()                  # It will only execute if we call this first
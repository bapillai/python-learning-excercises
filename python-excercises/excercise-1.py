# Write a Python Program that uses three variables.The variables in your program will be animal, vegetable and a mineral.Assign a string value to each one of the variables.Your program should display “Here is an animal, a vegetable, and a mineral.”Next, display the value for animal, followed by vegetable, and finally mineral. Each one of the values should be printed on their own line. Your program will display four lines in total
animal = "cat"
vegetable = "broccoli"
mineral = "gold"
sentence = animal + "  "+ vegetable + "  " + mineral + "."
print(sentence)
print(animal)
print(vegetable)
print(mineral)
print("--" * 16)



# Write a python program that prompts the user and simply repeats what the user entered.
userInput = input("Please type something and press enter: ")
print("You Entered: {}".format(userInput))
print("--" * 16)

# Write a Python program that prompts for input and displays a cat "saying" what was provided by the user. Place the input provided by the user inside a speech bubble. Make the speech bubble expand or contract to fit around the input provided by the user.
userInput = input("What do you want the cat to say: ")
print("-" * (len(userInput)+4))
print("< {} >".format(userInput))
print("-" * (len(userInput)+4))
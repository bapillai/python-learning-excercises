#Tuple
days_of_the_week = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
monday = days_of_the_week[0]
print(monday)
print()

for day in days_of_the_week:
    print(day)

# Uncomment the line below to see the error
 # TypeError: 'tuple' object does not support item assignment

# days_of_the_week[0] = "New Monday"
del days_of_the_week


weekend_tuple = ('Saturday','Sunday')
weekend_list = list(weekend_tuple)
print('weekend tuple is {}'.format(type(weekend_tuple)))
print('weekend list is {}'.format(type(weekend_list)))

for day in weekend_tuple:
    print(day)

weekend_days = ('Saturday','Sunday')
(sat, sun) = weekend_days
print(sat)
print(sun)

#List to Tuple assignment
contact_info = ['555-0123', 'jason@example.com']
(phone,email) = contact_info
print(phone)
print(email)

#How to use Tuple in a function
def high_and_low(numbers):
    """Determine the highest and lowest number"""
    highest = max(numbers)
    lowest = min(numbers)
    return (highest,lowest)

lottery_numbers = [16,4,42,15,23,8]
(highest, lowest) = high_and_low(lottery_numbers)
print("The highest number is {}".format(highest))
print("The lowest number is {}".format(lowest))

#Using tuples in a for loop
contacts = [('Jason','555-432'),('Carl','987-542')]
for (name,number) in contacts:
    print("the name is: {}".format(name))
    print("the number is: {}".format(number))

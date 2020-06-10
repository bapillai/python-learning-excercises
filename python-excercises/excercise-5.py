#Dictionary
contacts = { 'Jason': '555-0123', 'Carl': '555-0987'}
contacts['Tony'] = '555-0570'
print(contacts)
print(len(contacts))

#Deleting an element from Dictionary
del contacts['Jason']
print(contacts)

#Creating dictionary with additonal spaces in between elements
contacts = {
    'Jason': ['555-0123','555-0000'],
    'Carl': '555-0987'
}
print('Jason: ')
print(contacts['Jason'])
print('Carl: ')
print(contacts['Carl'])
for number in contacts['Jason']:
    print("The Phone is: {}".format(number))

contacts = {
    'Jason': ['555-0123','555-0000'],
    'Carl': '555-0987'
}
if 'Jason' in contacts.keys():
    print("Jason's contact is: ")
    print("{}".format(contacts['Jason']))
    print("{}".format(contacts['Jason'][0]))

if 'Carl' in contacts.keys():
    print("Carl's contact is: ")
    print("{}".format(contacts['Carl']))


if 'Tony' in contacts.keys():
    print("Tony's contact is: ")
    print("{}".format(contacts['Tony']))

#Dictionaries & For Loop
contacts = {
    'Jason': ['555-0123','555-0000'],
    'Carl': '555-0987'
}

for contact in contacts:
    print("The phone number of {0} is {1}".format(contact,contacts[contact]))

contacts = {
    'Jason': {
        'phone': '555-0123',
        'email': 'jason@example.com'
    },
    'Cark': {
        'phone': '555-0987',
        'email': 'carl@example.com'
    }
}

for contact in contacts:
    print("the contact is: {}".format(contact))
    print("the phone number is: {}".format(contacts[contact]['phone']))
    print("the phone number is: {}".format(contacts[contact]['email']))
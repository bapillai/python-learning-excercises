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
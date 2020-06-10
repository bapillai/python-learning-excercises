animals = ['man','bear','pig']
print(animals[0]) #man
animals[0] = 'cat'
print(animals[0]) #cat
print(animals[-1])#pig
print(animals[-2])#bear
print(animals[-3])#man
#In order to add elements to an existing list
animals.append('cow')
print(animals[-1])
#In order to add a new list or multiple elements into the existing list
more_animals = ['duck','lion']
animals.extend(more_animals)
print(animals)
animals.extend(['crow','eagle'])
print(animals)
#Inserting elements
animals.insert(0,'dove') #Pass the position where you want to insert the element and the element in itself
print(animals)
animals.insert(2,'pigeon')
print(animals) #['dove', 'cat', 'pigeon', 'bear', 'pig', 'cow', 'duck', 'lion', 'crow', 'eagle']

#Slice Method
animals = ['dove', 'cat', 'pigeon', 'bear', 'pig', 'cow', 'duck', 'lion', 'crow', 'eagle']
print("The new animals object is {}".format(animals))
some_animals = animals[1:4]
print(some_animals)
first_two_elements = animals[0:2]
print(first_two_elements)
first_two_elements_again = animals[:2]
print(first_two_elements_again)
last_two = animals[8:10]
print(last_two)
last_two_again = animals[-2:]
print(last_two_again)
all_except_last_two = animals[:-2]
print(all_except_last_two)

#String Slices
part_of_a_horse_string = 'horse'[1:4]
print(part_of_a_horse_string)

#Exception Handling
animals = ['man','bear','pig']
try:
    cat_index = animals.index('cat')
except:
    cat_index = 'No Cat found';
print(cat_index)





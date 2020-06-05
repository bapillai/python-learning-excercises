#For & while loop
animals = ['man','bear','pig','cow','duck','horse']
index = 0
while index < len(animals):
    print(animals[index])
    index += 1

for animal in animals:
    print(animal.upper())

#Sorted List
animals = ['man','bear','pig','cow','duck','horse']
sorted_animals = sorted(animals)
print(sorted_animals)
animals.sort()
print('Animals after using sort method: {}'.format(animals))
all_animals = sorted_animals + animals
print('Concatenated list of animals {}'.format(all_animals))
print(len(all_animals))
all_animals.append('eagle')
print(all_animals)
print(len(all_animals))

#Range Function
for number in range(3):
    print("Numbers in range where stop = 3: {}".format(number))

for number in range(1,10):
     print("Numbers in range where start = 1, stop = 10: {}".format(number))


for number in range(1,10,2):
     print("Numbers in range where start = 1, stop = 10, step = 2: {}".format(number))

animals = ['man','bear','pig','cow','duck','horse']
for number in range(0,len(animals),2):
    print(animals[number])


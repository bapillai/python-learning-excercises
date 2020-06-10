# Files
hosts = open('/etc/hosts')
host_file_contents = hosts.read()
print(host_file_contents)

# To go to the beginning of the file
hosts.seek(0)
# To go to the 5th byte position
hosts.seek(5)
# To provide the current position in the file
hosts.tell()

print('Files Closed? {}'.format(hosts.closed))
if not hosts.closed:
    hosts.close()
print('File closed? {}'.format(hosts.closed))

#Automatically close the file:
print('Start reading the file: ')
with open('/etc/hosts') as hosts:
    print('Files Closed? {}'.format(hosts.closed))
    print(hosts.read())
print('Finished reading the file')
print('File closed? : {}'.format(hosts.closed))

#Inorder read the contents of a file one line after another
with open('./File.txt') as hosts:
    for line in hosts:
        print(line)

# In the above code white space comes between lines of text because of the new line character that exists after the text on each line
with open('./File.txt') as hosts:
    for line in hosts:
        print(line.rstrip())

#Determing the mode of a file
with open('./File.txt') as file_name:
    print(file_name.mode)

# Writing data to a file
with open('./File.txt', 'w') as the_file:
    the_file.write("this text needs to be written to the file \n")
    the_file.write("here is more text.\n")

with open('./File.txt', 'r') as the_file:
    print(the_file.read())

#Reading binary files and accessing the code
with open('./File.txt', 'rb') as cat_picture:
    cat_picture.seek(2)
    cat_picture.read(4)
    print(cat_picture.tell())
    print(cat_picture.mode)

#Opening a file and assign its contents to a variable and handling all exception scenarios
try:
    contents = open('./contacts.txt',r).read()
except:
    contents = ''

print(len(contents))
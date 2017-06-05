import os

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = dir_name + '/example.txt'

if (os.path.isfile(file_name)):
    handler = open(file_name, 'r')

    # fetch all the content from the file
    content = handler.read()
    print(content)

    handler.seek(0)

    lines = handler.readlines()
    lines = [i.rstrip('\n') for i in lines]
    print(lines)

    handler.close()

    os.remove(file_name)

# the "w" - write mode will remove all the contents from a target file
handler = open(file_name, 'w')

for i in range(1, 7):
    handler.write('Line ' + str(i) + '\n')

handler.close()

# use the "a" - append mode to add more content to a file
handler = open(file_name, 'a')

for i in range(7, 11):
    handler.write('Apended line ' + str(i) + '\n')

handler.close()

with open(file_name, 'a+') as handler:
    handler.seek(0)
    first_line = handler.readline()
    handler.seek(os.SEEK_END)
    handler.write(first_line.rstrip('\n') + ' some new content\n')
    handler.close()


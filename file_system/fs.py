import os

dir_name = os.path.dirname(os.path.abspath(__file__))
handler = open(dir_name + '/example.txt', 'r')

# fetch all the content from the file
content = handler.read()
print(content)

handler.seek(0)

lines = handler.readlines()
lines = [i.rstrip('\n') for i in lines]
print(lines)

handler.close()

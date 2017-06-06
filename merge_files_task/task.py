import datetime
import os
import glob2

filename = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f.txt')

with open(filename, 'w') as merge_file:
    dir_name = os.path.dirname(os.path.abspath(__file__))

    for file_name in glob2.glob(os.path.dirname(os.path.abspath(__file__)) + '/file*.txt'):

        with open(file_name, 'r') as file_to_merge:
            merge_file.write(file_to_merge.read())
            file_to_merge.close()

    merge_file.close()

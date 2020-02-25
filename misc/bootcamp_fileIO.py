
##
##import os
##
##fName = 'Hello.txt'
##
##fPath = 'C:\\A\\'
##
##abPath = os.path.join(fPath, fName)
##print(abPath)


import os
import time

def find_txt_files_in_dir(directory):
    lst = os.listdir(directory)
    
    for i in lst:
        if i.endswith('txt'):
            print(os.path.join(directory, i))
            print('Last modified: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(directory +i))))     


if __name__ == "__main__":
    find_txt_files_in_dir('C:\\A\\')
    

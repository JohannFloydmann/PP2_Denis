import os
path = r'week6\dir-and-files\8py.txt'

if os.path.isfile(path):
    with open(path, 'w') as file:
        file.close()
        
    exists = os.access(path, os.F_OK)
    access = os.access(path, os.W_OK)
    if exists and access:
        os.remove(path)
        print("Deleted sucessfully")
    else:
        print("File doesn't exist or there is no access for deleting it")
else:
    print('It is not a file path')
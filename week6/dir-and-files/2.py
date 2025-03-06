import os 

file_name = r'week5\row.txt'

print('Existence: ', os.access(file_name, os.F_OK))
print('Readibility: ', os.access(file_name, os.R_OK))
print('Writability: ', os.access(file_name, os.W_OK))
print('Executability: ', os.access(file_name, os.X_OK))
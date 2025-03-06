st = input("Enter the words separated by spaces: ")
lt = st.split()

file_name = r'week6\dir-and-files\5py.txt'
with open(file_name, 'w') as file:
    for el in lt:
        file.write(el + '\n')
    file.close()

with open(file_name) as file:
    print(file.read())
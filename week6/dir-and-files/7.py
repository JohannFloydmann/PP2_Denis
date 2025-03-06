first = r'week6\dir-and-files\7py\first.txt'
second = r'week6\dir-and-files\7py\second.txt'

with open(first, 'w') as file:
    file.write("From the first file")
    file.close()

file = open(first)
content = file.read()
file.close()

with open(second, 'w') as file:
    file.write(content)
    file.close()

with open(second) as file:
    print(file.read())
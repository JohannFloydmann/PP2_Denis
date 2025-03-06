filename = r'week5\row.txt'
with open(filename, encoding='utf-8') as file:
    print(len(file.readlines()), 'lines')
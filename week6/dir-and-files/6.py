path = r'week6\dir-and-files\6py'

for i in range(65, 91):
    file = open(f"{path + '\\' + chr(i) + '.txt'}", 'w')
    file.close()
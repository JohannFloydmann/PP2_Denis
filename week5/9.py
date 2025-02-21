import re
test_string = 'eachWordShouldBeSeparated'
r = r'([A-Z])'

x = re.sub(r, lambda match: ' '+match.group(1), test_string)
print(x)
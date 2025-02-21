import re
test_string = 'this_is_snake_case'
r = r'_([a-z])'

x = re.sub(r, lambda match: match.group(1).upper(), test_string)
print(x)
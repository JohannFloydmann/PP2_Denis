import re
test_string = "thisIsACamelCase"
r = r'([A-Z])'

x = re.sub(r, lambda match:'_'+match.group(1).lower(), test_string)
print(x)
import re
test_string = "hell0AworldDpython"
r = r'[A-Z]'

x = re.split(r, test_string)
print(x)
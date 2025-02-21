import re

test_string = 'hello, world.'
r = r'[\s,.]'

x = re.sub(r, ':', test_string)
print(x)
import re

test_strings = ['ab', 'abb', 'abbb', 'abbbb']
r = r'ab{2,3}$'

for string in test_strings:
    if re.match(r, string):
        print(string, "matches")
    else:
        print(string, "doesn't match")
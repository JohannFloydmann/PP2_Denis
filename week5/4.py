import re

test_string = "HELLo woRLd HellO World StinFSfs"
r = r'[A-Z][a-z]+'

x = re.findall(r, test_string)
print(x)
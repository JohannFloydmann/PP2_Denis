import re

test_string = "test_string TeSt_StriNG TESt_sTRING"
r = r'[a-z]+_[a-z]+'

x = re.findall(r, test_string)
print(x)
import re

test_strings = ["a.....b",  "aaaaaaaaaaaaaaab", "abbbbbbbbbbbbbbbbbbbbbbb", "aioiob", "alohab", "a          b"]
r = r'a.*b'

for string in test_strings:
    if re.match(r, string):
        print(string, "matches")
    else:
        print(string, "doesn't match")
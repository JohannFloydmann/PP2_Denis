import re

test_strings = ["a", "ab", "abb", "ac", "b", "ba", "abc", "aab"]
r = r"ab*"

for string in test_strings:
    if re.match(r, string):
        print(string, "matches")
    else:
        print(string, "doesn't match")
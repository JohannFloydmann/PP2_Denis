def solve(heads, legs):
    r = (legs - 2*heads)/2
    c = heads - r
    return (r, c)

print(solve(35, 94))
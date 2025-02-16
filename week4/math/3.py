import math

def reg_pol(sides, length):
    return (sides * length * length) / (4 * math.tan(math.pi/sides))

n = int(input("Enter the number of sides: "))
l = int(input("Enter the length of one side: "))
print(reg_pol(n, l))
let = input("Enter the string: ")
up = 0
low = 0

for l in let:
    low += l.islower()
    up += l.isupper()

print("Upper:", up)
print("Lower:", low)
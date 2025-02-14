def down(n):
    while n >= 0:
        yield n
        n-=1

n = int(input("Enter the number: "))
for j in down(n):
    print(j, end=' ')
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

a = int(input("Enter the start number: "))
b = int(input("Enter the end number: "))
for j in squares(a, b):
    print(j, end=' ')
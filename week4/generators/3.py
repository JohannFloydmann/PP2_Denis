def thfr(n):
    for i in range(12, n+1, 12):
        yield i
            
n = int(input("Enter the number: "))
for j in thfr(n):
    print(j, end=' ')
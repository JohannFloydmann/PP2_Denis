def sq(n):
    for i in range (1, n+1):
        yield i*i
        
n = int(input("Enter the number: "))
for i in sq(n):
    print(i)
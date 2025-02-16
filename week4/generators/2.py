def even(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input("Enter the number: "))
flak = False
for j in even(n):
    if flak:
        print(', ', end='')
    flak = True
    print(j, end='')
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num//2):
        if num%i == 0:
            return False
    return True

def filter_prime(st):
    ls = st.split()
    ls = [int(x) for x in ls if isPrime(int(x))]
    return(ls)
    

print(filter_prime("5 2 0 10 10 3 1 253"))
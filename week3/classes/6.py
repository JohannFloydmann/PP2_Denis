def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num//2):
        if num%i == 0:
            return False
    return True

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 15, 17, 19, 29]
print(list(filter(lambda x: isPrime(x), nums)))
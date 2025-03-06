from math import sqrt
import time
num = int(input("Enter the number: "))
wait = int(input("Enter the waiting time: "))
time.sleep(wait*0.001)

print(f"Square root of {num} after {wait} miliseconds is {sqrt(num)}")
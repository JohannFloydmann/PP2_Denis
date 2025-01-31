from random import randint

num = randint(1, 21)
count = 1
name = input("Hello! What is your name?\n")

print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

while True:
    guess = int(input("Take a guess.\n"))
    print("\n")
    if guess == num:
        print(f"\nGood job, {name}! You guessed my number in {count} guesses!")
        break
    elif guess < num:
        print("Your guess is too low.")
        count+=1
    else:
        print("Your guess is too high.")
        count+=1
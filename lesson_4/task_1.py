from random import randint

random_int = randint(1, 10)
attempts = 0
max_attempts = 3

print(f"Hello, my friend! I've thought some number (between 1 and 10). Can you guess it?\n"
      f"You have {max_attempts} attempts")

while True:
    if attempts > max_attempts:
        print("Sorry, you don't have attempts to continue. Restart this program and try again.")
        break

    guess = input("Enter your number: ")

    if not guess.strip().isnumeric():
        attempts += 1
        print(f"You've entered not a number. Try again. | Attempts: {attempts}/{max_attempts}")
        continue

    guess = int(guess)
    if guess == random_int:
        print(f"You won! Yes, this was {guess}.\nCongratulations!!!")
        break

    if guess < random_int:
        attempts += 1
        print(f"Wrong number. My number is less | Attempts: {attempts}/{max_attempts}")
        continue

    if guess > random_int:
        attempts += 1
        print(f"Wrong number. My number is bigger | Attempts: {attempts}/{max_attempts}")
        continue


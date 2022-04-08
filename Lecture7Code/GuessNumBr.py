import random

#Generate a random number to be guessed
number = random.randint(0, 100) 
print(number)
print("Guess a magic number between 0 and 100")

while True: 
    #Prompt the user to guess the number
    guess = int(input("Enter your guess: "))

    if guess == number: 
        print("Yes, the number is " + str(number))
        break
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
import random
print("===== NUMBER GUESSING GAME ======")

secret_number = random.randint(1,100)
attempts = 0
max_attempts= 7
print("Guess a number between 1 and 100")
print("You have 7 attempts ")

while attempts < max_attempts:
    guess = int(input("\n Enter Your guess:"))
    attempts +=1

    if guess == secret_number:
        print("Congratulations You guesses correctly")
        print("Attempts used ",attempts)
        
        break
       
    elif guess <secret_number:
        print("Too low ! try a higher number")
    else:
        print("Too high ! try a lower number")

    remaining = max_attempts - attempts
    print("Reamainig attempts",remaining)

else:
    print("\n game over")
    print("the correct number was :",secret_number)
print("Thanks for playing")
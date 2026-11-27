
import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
draws = 0


def determine_winner(user, computer):

    if user == computer:
        return "draw"

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "user"

    else:
        return "computer"


print("===== ROCK PAPER SCISSORS =====")

while True:

    user = input(
        "\nEnter rock, paper, scissors or quit: "
    ).lower().strip()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("Your choice:", user)
    print("Computer choice:", computer)

    winner = determine_winner(user, computer)

    if winner == "draw":
        print("It's a draw!")
        draws += 1

    elif winner == "user":
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("\n===== SCOREBOARD =====")
    print("Your score:", user_score)
    print("Computer score:", computer_score)
    print("Draws:", draws)


print("\n===== FINAL RESULT =====")

print("Your wins:", user_score)
print("Computer wins:", computer_score)
print("Total draws:", draws)

if user_score > computer_score:
    print("Congratulations! You won the game!")

elif computer_score > user_score:
    print("Computer won the game!")

else:
    print("The game ended in a draw!")

print("Thanks for playing!")

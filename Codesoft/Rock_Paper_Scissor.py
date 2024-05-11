import random

def main():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        print("\nChoose your weapon!")
        user_input = input("Enter rock, paper, or scissors: ").lower()

        while user_input not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_input = input("Enter rock, paper, or scissors: ").lower()

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_input == computer_choice:
            print("It's a tie!")
        elif (user_input == "rock" and computer_choice == "scissors") or \
             (user_input == "paper" and computer_choice == "rock") or \
             (user_input == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

        if input("Play again? (yes/no): ").lower() != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

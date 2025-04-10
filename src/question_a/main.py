from question_a import get_random_number

def main():
    print("Welcome to the Guessing Game!") 

    while True:
        number = get_random_number()
        print("\nI'm thinking of a number between 1 and 5.")

        while True:
            try:
                guess = int(input("Your guess: "))
                if guess < 1 or guess > 5:
                    print("Please guess a number between 1 and 5.")
                    continue
                if guess == number:
                    print("Correct! Nice job!")
                    break
                else:
                    print("Not quite. Try again!")
            except ValueError:
                print("Please enter a valid integer.")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()


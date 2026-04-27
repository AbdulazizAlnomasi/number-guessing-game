import random

def get_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy (15 attempts, range 1-50)")
    print("2. Medium (10 attempts, range 1-100)")
    print("3. Hard (5 attempts, range 1-200)")
    
    while True:
        try:
            choice = int(input("Enter 1, 2, or 3: "))
            if choice == 1:
                return 15, 1, 50
            elif choice == 2:
                return 10, 1, 100
            elif choice == 3:
                return 5, 1, 200
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def number_guessing_game():
    print("=" * 50)
    print("        WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 50)
    
    total_games = 0
    total_attempts = 0
    
    while True:
        max_attempts, min_range, max_range = get_difficulty()
        secret_number = random.randint(min_range, max_range)
        attempts = 0
        game_won = False
        
        print(f"\nI'm thinking of a number between {min_range} and {max_range}.")
        print(f"You have {max_attempts} attempts to guess it.\n")
        
        while attempts < max_attempts:
            try:
                guess = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")
                guess = int(guess)
                
                if guess < min_range or guess > max_range:
                    print(f"Please enter a number between {min_range} and {max_range}.\n")
                    continue
                
                attempts += 1
                
                if guess < secret_number:
                    print("Too low! Try a higher number.\n")
                elif guess > secret_number:
                    print("Too high! Try a lower number.\n")
                else:
                    print(f"\n{'=' * 50}")
                    print(f"  CONGRATULATIONS! You guessed it in {attempts} attempts!")
                    print(f"  The number was {secret_number}.")
                    print(f"{'=' * 50}")
                    game_won = True
                    total_games += 1
                    total_attempts += attempts
                    break
                    
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")
        
        if not game_won:
            print(f"\n{'=' * 50}")
            print(f"  GAME OVER! You ran out of attempts.")
            print(f"  The number was {secret_number}.")
            print(f"{'=' * 50}")
            total_games += 1
            total_attempts += attempts
        
        if total_games > 0:
            avg_attempts = total_attempts / total_games
            print(f"\nStatistics - Games Played: {total_games} | Average Attempts: {avg_attempts:.1f}")
        
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again == 'yes' or play_again == 'y':
                print("\n" + "=" * 50)
                break
            elif play_again == 'no' or play_again == 'n':
                print("\n" + "=" * 50)
                print("     THANK YOU FOR PLAYING! GOODBYE!")
                print("=" * 50)
                return
            else:
                print("Please enter 'yes' or 'no'.")
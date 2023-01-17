import random

def generate_number():
    # Generate a random 3-digit number with no repeating digits
    digits = list(range(1, 10))
    random.shuffle(digits)
    return digits[:3]

def get_user_guess():
    # Get a 3-digit guess from the user
    while True:
        guess = input("Enter a 3-digit number: ")
        if len(guess) != 3:
            print("Invalid input. Please enter a 3-digit number.")
        elif not guess.isnumeric():
            print("Invalid input. Please enter a number.")
        elif len(set(guess)) != 3:
            print("Invalid input. Please enter a 3-digit number with no repeating digits.")
        else:
            return [int(d) for d in guess]

def evaluate_guess(guess, target):
    # Evaluate the guess and return the number of strikes and balls
    strikes = 0
    balls = 0
    for i, d in enumerate(guess):
        if d == target[i]:
            strikes += 1
        elif d in target:
            balls += 1
    return (strikes, balls)

def play_game():
    # Play a game of baseball
    target = generate_number()
    print("Welcome to baseball! Guess the 3-digit number.")
    strikes = 0
    balls = 0
    while strikes < 3:
        guess = get_user_guess()
        strikes, balls = evaluate_guess(guess, target)
        print("Strikes:", strikes)
        print("Balls:", balls)
    print("You win!")

play_game()
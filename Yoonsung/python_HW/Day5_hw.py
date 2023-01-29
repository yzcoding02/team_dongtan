# import random

# def generate_number():
#     # Generate a random 3-digit number with no repeating digits
#     digits = list(range(1, 10))
#     random.shuffle(digits)
#     return digits[:3]

# def get_user_guess():
#     # Get a 3-digit guess from the user
#     while True:
#         guess = input("Enter a 3-digit number: ")
#         if len(guess) != 3:
#             print("Invalid input. Please enter a 3-digit number.")
#         elif not guess.isnumeric():
#             print("Invalid input. Please enter a number.")
#         elif len(set(guess)) != 3:
#             print("Invalid input. Please enter a 3-digit number with no repeating digits.")
#         else:
#             return [int(d) for d in guess]

# def evaluate_guess(guess, target):
#     # Evaluate the guess and return the number of strikes and balls
#     strikes = 0
#     balls = 0
#     for i, d in enumerate(guess):
#         if d == target[i]:
#             strikes += 1
#         elif d in target:
#             balls += 1
#     return (strikes, balls)

# def play_game():
#     # Play a game of baseball
#     target = generate_number()
#     print("Welcome to baseball! Guess the 3-digit number.")
#     strikes = 0
#     balls = 0
#     while strikes < 3:
#         guess = get_user_guess()
#         strikes, balls = evaluate_guess(guess, target)
#         print("Strikes:", strikes)
#         print("Balls:", balls)
#     print("You win!")

# play_game()

import random

def play_game():
    number_of_rounds = int(input("몇 라운드를 하시겠습니까? "))
    total_score = 0

    for round_number in range(1, number_of_rounds + 1):
        print("Round {}:".format(round_number))
        secret_number = random.randint(1, 10)
        print("1부터 10 사이의 숫자를 맞춰보세요.")
        guess = int(input("추측한 숫자를 입력하세요: "))
        if guess == secret_number:
            print("맞았습니다!")
            total_score += 1
        else:
            print("틀렸습니다. 정답은 {}입니다.".format(secret_number))

    print("게임이 종료되었습니다. 총 점수는 {}점 입니다.".format(total_score))

play_game()
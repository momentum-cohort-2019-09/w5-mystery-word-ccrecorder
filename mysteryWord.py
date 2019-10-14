import random
letter_guesses = []


def end_game():
    with open("words.txt") as words_list:
        words = words_list.read().split()
    easy_words = []
    medium_words = []
    hard_words = []
    expert_words = []
    for word in words:
        if len(word) == 4 or len(word) == 5:
            easy_words.append(word)
        elif len(word) == 6 or len(word) == 7:
            medium_words.append(word)
        elif len(word) == 7 or len(word) == 8:
            hard_words.append(word)
        elif len(word) > 8:
            expert_words.append(word)
    print(
        "Welcome to the cutest little guessing game. To exit, press [ctrl + d]. Good luck! :)")
    level = input(
        "Choose your level: easy, medium, hard, or expert => ")
    if level == "easy":
        answer = random.choice(easy_words).lower()
    elif level == "medium":
        answer = random.choice(medium_words).lower()
    elif level == "hard":
        answer = random.choice(hard_words).lower()
    elif level == "expert":
        answer = random.choice(expert_words).lower()
    # answer = random.choice(words).lower()
    print(answer)
    print("This word has", len(answer), "letters!")
    board = ['_'] * len(answer)
    game_over = False
    print(" ".join(board))

    def compare_letter(word, board, guess):
        start = 0
        if word.find(guess, start) == -1:
            letter_guesses.append(guess)
            print("Oops, try another letter or word.")
        else:
            while word.find(guess, start) != -1:
                index = word.index(guess, start)
                start = index + 1
                board[index] = guess
            return board

    while (game_over == False):
        if answer == ("".join(board)):
            print("YOU WIN MOFO")
            print("Press up and enter to play again.")
            return
        else:
            if len(letter_guesses) >= 8:
                print("GAME OVER LOSERRRR")
                print("The word was", answer)
                print("Press up and enter to play again.")
                return
            else:
                print("Incorrect guesses:", ", ".join(letter_guesses))
                print("You have", 8-len(letter_guesses), "guesses remaining.")
                guess = input("Guess a letter or word :)  ")
                if len(guess) == 1 and guess.isalpha():
                    compare_letter(answer, board, guess)
                    print(" ".join(board))
                elif len(guess) == len(answer) and guess.isalpha():
                    board2 = []
                    if guess == answer:
                        print(
                            "Wow! You win! Press the up arrow and hit enter to play again. :) ")
                        for letter in guess:
                            board2.append(letter)
                            board = board2
                            return board
                    else:
                        letter_guesses.append(guess)
                        print(" ".join(board))
                else:
                    print("Oops, that's not a valid guess. :/ Try again. ")
                    print(" ".join(board))
                    guess = input("Guess a letter or word :)  ")


end_game()
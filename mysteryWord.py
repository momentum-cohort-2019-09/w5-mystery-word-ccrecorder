import random

with open("words.txt") as words_list:
  words = words_list.read().split()

answer = random.choice(words)
answer_letters = list(answer)
print("This word has", len(answer), "letters!")
board = ['_ ' * len(answer)]
print(board[0])

wrong_guesses = 0
letter_guesses = []
word_guesses = []

def compare_letter(guess):
  wrong_guesses = 0
  if guess in answer_letters:
    print("that is good")
  else:
    wrong_guesses += 1
    print("You wrong, you have", 8 - wrong_guesses, "guesses left!")
    
guess = input("guess a letter -->")

compare_letter(guess)

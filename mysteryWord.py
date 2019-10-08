import random

with open("words.txt") as words_list:
  words = words_list.read().split()

def random_word():
  return random.choice(words)
  
  
  
print(random_word())

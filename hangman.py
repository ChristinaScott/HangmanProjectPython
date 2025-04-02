import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# chose word for game from list of words and print
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
placeholder = ""

#print(chosen_word) #optional

#generate a placeholder list with as many items as the chosen word
amount_of_letters = len(chosen_word)
for each in range(amount_of_letters):
    placeholder += "-"
print(placeholder)

game_over = False
already_guessed_letters = []
lives = 6

while not game_over:
    # ask user to choose letter and save as variariable.  make it lowercase
    chosen_letter = str.lower(input("Choose a letter: "))

    # loop through chosen word and write matches or dashes to emtpy string

    if chosen_letter in already_guessed_letters:
        print(f"You already guessed {chosen_letter}. Go again")
    elif chosen_letter not in already_guessed_letters and chosen_letter not in chosen_word:
        already_guessed_letters.append(chosen_letter)
        lives -= 1
    
    display = ""
    for char in chosen_word:
        if char == chosen_letter:
            display += char
            already_guessed_letters.append(char)
        elif char in already_guessed_letters:
            display += char
            already_guessed_letters.append(char)
        else:
            display += "-"
    
    print(stages[lives])
    print(display)
    if chosen_letter not in chosen_word:
        print(f"'{chosen_letter}' in not in this word. You loose a life")
    print(f"you have {lives} lives left!")
    

    # winning condition to exit while loop
    if "-" not in display:
        game_over = True
        print("You win!")

    #loosing condition to exit while loop
    if lives == 0:
        game_over = True
        print("You loose!")
#importing modules
import random
from game_art import pieces, logo, win
import game_words
from piece_loss import message

# Clear screen
print("\033[H\033[J", end="")

#Welcome message
print("I am Abhigyan!\nHope you enjoy my game!")

#Logo
print(logo)

#Choosing the word
chosen_word = random.choice(game_words.word_list)
lives = 6

#Showing the blank
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

#setting up variables
game_over = False
game_win = False
correct_letters = []

#Program start
while not game_over:

    # Number of lives left
    print(f"{lives}/6 LIVES LEFT")
    guess = input("Guess a letter:\n").lower()

    # Check the guessed letter
    display = ""
    if guess in correct_letters:
        print(f'Oh! You have already guessed {guess}')
    elif guess in chosen_word:  
        print(f'Yay! You guessed {guess} which is in the word!')     

    #Checking everything
    #Core logic of the game
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    #Loss of life
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True    
        print(f'Oh no!\nYou guessed {guess} which is not in the word!\n{message[lives]}')

    #Win condition
    if "_" not in display:
        game_over = True
        print(win)
        game_win = True

    # Printing the stages of the game
    if game_win == False:
        print(pieces[lives])

    # Show the progress
    if game_over == False:
        print("Word to guess: " + display)

    # Show the word if the game is over
    if game_over == True and lives == 0:
        print(f"The word was '{chosen_word}'")

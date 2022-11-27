
from replit import clear
import random
from hangman_words import word_list

chosen_word = random.choice(word_list) 
word_length = len(chosen_word) 
end_of_game = False 

lives = 6 

#Now lets Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages
print(logo)
display = []

for _ in range(word_length): 
    display.append("_")
    # display += "_" # or we can use display.append("_")

while not end_of_game: 
    guess = input("Guess a letter: ").lower()
    clear() 
  #Let's Check the guessed letter
    for position in range(word_length):
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if chosen_word[position] == guess:
            display[position] = chosen_word[position] 

    #Let's check if the user is wrong. 
          #Now If the letter guessed is not in the chosen_word, we are going to print out the letter and let the user know it's not in the word.
    if guess not in chosen_word: 
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1 
        if lives == 0: # as we have seen that the life stages in a list are 6, so now we need to count them down to zero and if the lives is zero the game is over. 
            end_of_game = True 
            print("You lose.")
    #Lef check If the user has entered a letter they've already guessed,  and we print the letter and let them know.:
    if guess in display:
        print(f"You've already guessed {guess}")

    #Now let's Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # and lastly let's Check if the user has got all letters, so that he/she won the game:
    if "_" not in display:
        end_of_game = True  
        print("You win.")

    # from hangman_art import stages
    print(stages[lives])
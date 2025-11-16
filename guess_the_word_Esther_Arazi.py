'''
By: Esther Arazi

This program gives the user a word to guess based on the user's input
of level and catagory choice. Additionally, keeps track of the user's
wins and losses while playing the game.

'''

WINS = 0 # Tracks the number of wins
LOSSES = 0 # Tracks the number losses
TRIES_LFT = 10 # Tracks the amount of tries the user has left
WRONG_CHS = [] # A list of the wrong characters chosen by the user
CRCT_CHS = [] # A list of the correct characters chosen by the user
CHOSEN_WRD = ['_'] # The blank spaces used to fill when guessing the word

# Three "dictionaries of catagories and within the level choices
animals = {
    'easy': ['monkey', 'rabbit', 'spider', 'jaguar', 'parrot'],
    'medium': ['elephant', 'anteater', 'kangaroo', 'chipmunk'],
    'hard': ['grasshopper', 'woodpecker', 'rattlesnake', 'salamander']
}

sports = {
    'easy': ['soccer','karate','hockey','tennis','skiing'],
    'medium': ['baseball','swimming','football','lacrosse'],
    'hard': ['basketball', 'volleyball','cheerleading','kickboxing']
}

foods = {
    'easy': ['tomato', 'muffin', 'banana', 'potato','orange'],
    'medium': ['oatmeal','eggplant', 'cucumber','sandwich'],
    'hard': ['cheesecake','watermelon','peppermint', 'cappuccino']
}

categories = [animals, sports, foods] # Allows that all the three categories to be one dictionary

animals_e = categories[0]['easy'] # Each catagory is separated based on the list and level
animals_m = categories[0]['medium']
animals_h = categories[0]['hard']

sports_e = categories[1]['easy']
sports_m = categories[1]['medium']
sports_h = categories[1]['hard']

food_e = categories[2]['easy']
food_m = categories[2]['medium']
food_h = categories[2]['hard']

#---------- TODO ----------
import random

def user_input_str(prompt, allowed):
    '''
    This function ensures that the user's input is a string.
    Prompt the user the questions of level and catagory choice.

    :param prompt: The Questions
    :param allowed: The given answers, so that valid answers are the catagories and level choices.
    :return: evaluates the user's input if it is valid
    '''

    allowed_lower = [a.lower() for a in allowed]
    prompt = prompt + str(allowed_lower) + ': '
    while True:
        try:
            user_input = input(prompt).lower().strip()
            if user_input not in allowed_lower:
                raise ValueError('Invalid Input')
            return user_input
        except ValueError:
            print('Invalid Input — please try again.')


def user_level_animal_choice(level):
    '''
    Based on the user's input, if the user asked for the "animals" catagory and based
    on the level choice, the game prompts the "secret word" to the user.
    :param level: Based on user's level choice
    :return: the level word of that catagory
    '''

    if level == 'easy':
        return random.choice(animals_e) # Gives a random easy word in this catagory
    elif level == 'medium':
        return random.choice(animals_m) # Gives a random medium - level word in this catagory
    else:
        return random.choice(animals_h) # Gives a random hard word in this catagory


def user_level_food_choice(level):
    '''
    Based on the user's input, if the user asked for the "foods" catagory and based
    on the level choice, the game prompts the "secret word" to the user.
    :param level: Based on user's level choice
    :return: the level word of that catagory
    '''

    if level == 'easy':
        return random.choice(food_e) # Gives a random easy word in this catagory
    elif level == 'medium':
        return random.choice(food_m) # Gives a random medium - level word in this catagory
    else:
        return random.choice(food_h) # Gives a random hard word in this catagory


def user_level_sports_choice(level):
    '''
       Based on the user's input, if the user asked for the "foods" catagory and based
       on the level choice, the game prompts the "secret word" to the user.
       :param level: Based on user's level choice
       :return: the level word of that catagory
       '''

    if level == 'easy':
        return random.choice(sports_e) # Gives a random easy word in this catagory
    elif level == 'medium':
        return random.choice(sports_m) # Gives a random medium - level word in this catagory
    else:
        return random.choice(sports_h) # Gives a random hard word in this catagory


def user_category_choice(level, category):
    '''
    Based on the user's level choice and catagory choice,
    the game propmt the user the "secret word".
    :param level: user's level choice.
    :param category: user's catagory choice.
    :return: the catagory choice
    '''

    if category == 'sports':
        return user_level_sports_choice(level)
    elif category == 'foods':
        return user_level_food_choice(level)
    elif category == 'animals':
        return user_level_animal_choice(level)
    else:
        print('Invalid Input')


#------------ Evaluate User Input -----------

def eval_user_input(guess_lttr, secret_word):
    '''
    This function evaluates the user's inputs and guesses.
    :param guess_lttr: The user's input, either letter or if they guess the word
    :param secret_word: The chosen word for the user to guess.
    :return: ensure that the user's guesses are valid.
    '''

    global WINS, LOSSES, TRIES_LFT, WRONG_CHS, CRCT_CHS, CHOSEN_WRD

    # If the full word was guessed - based on full word input
    if guess_lttr == secret_word:
        print()
        print(f'Congrats! You guessed the word! - "{secret_word}"')
        WINS += 1
        print(
            f'Wins: {WINS}    Losses: {LOSSES}    Tries Left: {TRIES_LFT}'
        )
        return True

    #If the user guesses and incorrect word
    if len(guess_lttr) > 1 and guess_lttr.isalpha() and guess_lttr != secret_word:
        TRIES_LFT -= 1
        print()
        print(f'Incorrect word guess! "{guess_lttr}" is not the secret word.')
        print(f'Tries left: {TRIES_LFT}')

    #Single letter guesses -- either right or wrong
    elif len(guess_lttr) == 1 and guess_lttr.isalpha():

        # if user guessed a letter already
        if guess_lttr in CRCT_CHS or guess_lttr in WRONG_CHS:
            print()
            print(f"You already guessed '{guess_lttr}'. Choose a new letter.")
            print(f'Tries left: {TRIES_LFT}')
            print()
            print(' '.join(CHOSEN_WRD))
            return False

        # if user guessed a correct letter
        if guess_lttr in secret_word:

            # reveals correct letters
            for index, character in enumerate(secret_word):
                if character == guess_lttr:
                    CHOSEN_WRD[index] = character

            if guess_lttr not in CRCT_CHS:
                CRCT_CHS.append(guess_lttr)
                print()
                print(f'You guessed correctly!')
                print(f'Tries left: {TRIES_LFT}')
                print(' '.join(CHOSEN_WRD))

            #check if full word was guessed - based on letter inputs
            if '_' not in CHOSEN_WRD:
                print()
                print(f'Congrats! You guessed the word! - "{secret_word}"')
                WINS += 1
                print(
                    f'Wins: {WINS}    Losses: {LOSSES}    Tries Left: {TRIES_LFT}'
                )
                return True

        else:

            # Prevents duplicates in wrong guesses
            if guess_lttr not in WRONG_CHS:
                WRONG_CHS.append(guess_lttr)
                TRIES_LFT -= 1
                print()
                print(f'Tries left: {TRIES_LFT}')
                print(f'Try again. You chose: {WRONG_CHS}')
                print()
                print(' '.join(CHOSEN_WRD))

            # When user is out of tries
            if TRIES_LFT == 0:
                print()
                print(f"You're out of tries! The word was: {secret_word}")
                LOSSES += 1
                print(
                    f'Wins: {WINS}    Losses: {LOSSES}    Tries Left: {TRIES_LFT}'
                )
                return True
    else:
        print()
        print('Invalid input.')


# -------- Loops Question ----------

def word_letter_guesses(secret_word):
    '''
    This function prompts the user to "guess the word" -- either inputting a letter or
    to guess the word
    :param secret_word: The chosen word for the user to guess.
    '''
    while True:
        print()
        guess_lttr = input('Guess a letter or input the word: ').lower().strip()

        # Calls the evaluator function
        done = eval_user_input(guess_lttr, secret_word)

        if done:  # if True == game over -- when user guesses the word
            break


def game_restart():
    '''
    This function resets the tries, the lists: the wrong and correct letters, and the
    list that is used for the blank line to fill in the word.
    '''

    global TRIES_LFT, WRONG_CHS, CRCT_CHS, CHOSEN_WRD
    # resets game
    TRIES_LFT = 10
    WRONG_CHS = []
    CRCT_CHS = []
    CHOSEN_WRD = ['_']


#---------- Main Program ----------

def main():
    '''
    The main funcion of the program and where the game runs.
    '''

    global CHOSEN_WRD

    while True: # Used to rerun game if user chooses to play again.
        game_restart()
        print()
        print('Welcome to Guess the Word!')

        # Asks the user what level to play
        level = user_input_str(
            'Choose a level to play: ', ['Easy', 'Medium', 'Hard']
        )

        # Asks the user what category to play
        category = user_input_str(
            'Choose a catagory: ', ['Sports', 'Foods', 'Animals']
        )
        print()

        secret_word = user_category_choice(level, category) # Chooses the chosen word for the user

        CHOSEN_WRD = ['_'] * len(secret_word) # Creates the list of underscores - "_"
        print(' '.join(CHOSEN_WRD))

        word_letter_guesses(secret_word)
        print()

        # Asks the user if they want to play again or not
        user_restart = (
            user_input_str('Want to play again?', ['yes', 'no'])
        )

        if user_restart == 'yes':
            continue

        elif user_restart == 'no':
            print()
            print('Thanks for playing!')
            print(
                f'Wins: {WINS}    Losses: {LOSSES}    Tries Left: {TRIES_LFT}'
            )
            break
        else:
            print('Invalid Input')


if __name__ == '__main__':
    main()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word += ' _ '
        else:
            guessed_word += letter
    return guessed_word

def warnings_count(user_input,u_input,warnings,guess,guessed_word):
    if user_input.isalpha() == False and warnings >= 0:
        print("Oops! That is not a valid letter")
        print('You have {} warnings left'.format(warnings))
        print(guessed_word)
        print('_____________________________________________________')
    elif user_input in u_input and warnings >= 0:
        print('Oops! you\'ve already guessed that letter')
        print('You have {} warnings left'.format(warnings))
        print(guessed_word)
        print('_____________________________________________________')
    elif user_input.isalpha() == False and warnings < 0 :
        print("Oops! That is not a valid letter")
        print('You have no warning left')
        print(guessed_word)
        print('_____________________________________________________')
    elif user_input in u_input and warnings < 0:
        print('Oops! you\'ve already guessed that letter')
        print('You have no warnings left'.format(warnings))
        print(guessed_word)
        print('_____________________________________________________')
    return ''



import string
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str = string.ascii_lowercase
    for letter in letters_guessed:
        if letter in string.ascii_lowercase:
            str = str.replace(letter,'')
    return str
def welcomemessage(warnings,secret_word):
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long'.format(str(len(secret_word))))
    print('You have {} warnings left'.format(warnings))
    print('_____________________________________________________')
def endmessage(guess,secret_word):
    if guess > 0:
        print('Congratualtions, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was {}'.format(secret_word))
    return ''
def hangman(secret_word):
    guess = 6
    word = ''
    guessed_word = ''
    u_input = []
    warnings = 3
    vowel = ['a','e','i','o','u']
    welcome = welcomemessage(warnings,secret_word)
    while guess > 0 and not is_word_guessed(secret_word,u_input):
        available_letters = get_available_letters(u_input)
        print('\nYou have {} guesses left.'.format(guess))
        print('Available_letters: ' +available_letters)
        user_input = input('Please guess a letter: ')
        if (user_input.isalpha()) == True:
            if user_input not in u_input:
                u_input += user_input.lower()
                guessed_word = get_guessed_word(secret_word,u_input)

                if user_input  in secret_word:
                    print('Good guess:  ' +guessed_word)
                else:
                    print('Oops! That letter is not in my word: ' +guessed_word)
                if user_input in vowel and user_input not in secret_word:
                    guess -= 2
                elif  user_input not in vowel and user_input not in secret_word:
                    guess -= 1

                print('_____________________________________________________')
            else:
                war = warnings_count(user_input,u_input,warnings,guess,guessed_word)
                print(war)
                warnings -= 1
                if warnings < 0:
                    guess -= 1

        else:
            war = warnings_count(user_input,u_input,warnings,guess,guessed_word)
            print(war)
            warnings -= 1
            if warnings < 0:
                guess -= 1

    print(endmessage(guess,secret_word))
    return ''
print(hangman('apple'))

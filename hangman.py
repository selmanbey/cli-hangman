from random import choice
from random import randint

wordList = ['ANGEL', 'DEEP', 'CREATION', 'SEMINAR', 'BATH', 'GLISTENING', 'CAUSE', 'KNOT', 'FRIGHTEN', 'UPBEAT', 'CALLOUS', 'CAVE', 'OCEAN', 'CLOISTERED', 'SCARE', 'BASE', 'GAINFUL', 'BOLT', 'PLASTIC', 'DESIGN', 'INCREASE', 'CLEAR', 'TRUST', 'COUNTRY', 'RISK', 'QUINCE', 'CROSS', 'ANXIOUS', 'POLITE', 'SMOKE', 'AMUSEMENT', 'CAKE', 'EXOTIC', 'OUTGOING', 'SPRAY', 'RUDDY', 'CHASE', 'QUIET', 'TEAM', 'ADMIRE', 'LAUGH', 'FIERCE', 'NOXIOUS', 'WANDER', 'MEMORISE', 'STROKE', 'WITTY', 'HEARTBREAKING', 'UNARMED', 'HARASS', 'AFRAID', 'UNDERWEAR', 'NUMBERLESS', 'PRECEDE', 'LIQUID', 'FOLD', 'NATURAL', 'FEARFUL', 'FRANTIC', 'BROKEN', 'MODERN', 'ANSWER', 'REFUSE', 'PHONE', 'COMMAND', 'ANGLE', 'SAME', 'HOUSES', 'GIGANTIC', 'HANDY', 'FLAGRANT', 'STINGY', 'HOOK', 'ADD', 'TAWDRY', 'PEST', 'BUSY', 'APPAREL', 'SIMPLE', 'GOOFY', 'FASCINATED', 'GREEN', 'SMILE', 'CALM', 'WIDE', 'GROUND', 'SCARCE', 'RITZY', 'BLIND', 'STOCKING', 'CRATE', 'MINOR', 'GRIP', 'CONCENTRATE', 'TASTE', 'LICK', 'BACK', 'TOUGH', 'SPOTTED', 'GROOMED', 'OBTAIN', 'COPY', 'GUITAR']

secretWord = choice(wordList)
guessedWord = secretWord #Just to keep the original while altering the word with right guesses
board = []
guessedLetters = []
if len(secretWord) <= 6: #To give the user more chances in longer words, but never more than 7
    chances = len(secretWord) + 1
else:
    chances = 7

#STARTING SCREEN
print "PYTHON HANGMAN\nClassic Hangman Game in Python (Text-Only Version)\nHere is your secret word:\n"

for l in secretWord:
    board.append("_")
print ' '.join(board)
print "\nYou can have %d guesses for this word" % (chances)

user_guess = raw_input("To make your first guess, please enter a letter: ")
while not user_guess.isalpha() or len(user_guess) != 1:
    user_guess = raw_input ("I'm afraid that's not a proper letter.\nPlease try again: ")
user_guess = user_guess.upper()


#GAMEPLAY
while chances > 1:
    if guessedWord == str('0' * len(secretWord)):
        print "CONGRATULATIONS!"
        print secretWord + " WAS INDEED THE WORD! GOOD JOB!"
        break
    while user_guess in guessedLetters:
        print ' '.join(board)
        user_guess = raw_input("You've already guessed that, remember?\nThis doesn't count, give it another go: ")
        user_guess = user_guess.upper()
    else:
        chances -= 1
        if user_guess in guessedWord:
            chances += 1
            repeats = guessedWord.count(user_guess) #checks how many times user_guess occur in secretWord
            index = guessedWord.find(user_guess) #finds user_guess' first appearance
            if repeats == 1:
                for letter in guessedWord:
                    if letter == user_guess:
                        guessedWord = guessedWord.replace(letter, '0')
                        board[index] = user_guess
                        print 'Congratulations! You got a letter!'
                        print ' '.join(board)
                        guessedLetters.append(user_guess)
            else:
                while user_guess in guessedWord:
                    for letter in guessedWord:
                        if letter == user_guess:
                            index = guessedWord.find(user_guess)
                            guessedWord = guessedWord.replace(letter, '0', 1)
                            board[index] = user_guess
                    print 'Congratulations! You got %d letter!' % (repeats)
                    print ' '.join(board)
                    guessedLetters.append(user_guess)
            if guessedWord != str('0' * len(secretWord)):
                user_guess = raw_input("Enter another letter: ")
                while not user_guess.isalpha() or len(user_guess) != 1:
                    user_guess = raw_input ("That is not a proper letter.\nPlease try again: ")
                user_guess = user_guess.upper()
        else:
            guessedLetters.append(user_guess)
            print ' '.join(board)
            print 'Chances Left: ' + str(chances)
            user_guess = raw_input("Didn't work out this time.\nMaybe try again?: ")
            while not user_guess.isalpha() or len(user_guess) != 1:
                user_guess = raw_input ("That is not a proper letter.\nPlease try again: ")
            user_guess = user_guess.upper()
if guessedWord != str('0' * len(secretWord)):
    print "No more chances left.\nSorry, buddy.\nGame Over!\nThe word was '%s', just in case if you're wondering" % (secretWord)

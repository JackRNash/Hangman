import random

# Global vars
MAX_GUESSES = 7
lettersGuessed = []
txt = open('wordsEn.txt').readlines()

def chooseWord():
    arr = []
    for line in txt:
        arr.append(line[:-1])
    index = random.randint(0, len(arr) - 1)
    return arr[index]


def howManyGuesses(guesses):
    while not guesses.isdigit():  # error checking
        guesses = input("Please put in a number and only a number.\n")
    return int(guesses)


def isValidGuess(guess):
    if len(guess) != 1 or not guess.isalpha():  # if not letter, not valid
        print("Sorry, please input a single character.")
        return False
    if guess in lettersGuessed:  # if already guessed, not valid
        print("You already guessed " + str(guess) + ". Please try another letter.")
        return False
    return True


def playHangman():
    wants_to_play = True #keep track of if user wants to multiple times
    while wants_to_play:
        # set up word
        word = chooseWord()  # pick word they're guessing for
        guessedWord = list("_ " * len(word))

        print("Welcome to Jack's Hangman! You will try to guess the word to save a man's life!\n")

        # Figure out how many guesses they have
        guesses = input("How many answers would you like to be able to get wrong and still be able to win?\n")
        guesses = howManyGuesses(guesses)
        while guesses > MAX_GUESSES:
            guesses = input("There's no time! Choose a lower number!\n")
            guesses = howManyGuesses(guesses)

        # gameplay loop
        guessed = 0
        won = False
        hasGuessed = False #used to not display guessed letters on first iteration

        while guessed < guesses:
            print("\n\nYou can spare " + str(guesses - guessed) + " wong answers. Here's what we know so far\n" + "".join(
                guessedWord)) if guesses - guessed > 1  or guesses - guessed == 0\
                else print("\n\nYou can spare " + str(guesses - guessed) + " wrong ansers. Here's what we know so far\n" + "".join(guessedWord))
            if hasGuessed:
                print("So far you've guessed: " + "".join(lettersGuessed))
            # get guess
            g = input("What would you like to guess?\n")
            while not isValidGuess(g):
                g = input("What will your new guess be?\n")
            g = g.lower()

            # process of updating word
            if len(lettersGuessed) >= 1:  # formatting for user display
                lettersGuessed.append(", ")
                lettersGuessed.append(g)
            else:
                lettersGuessed.append(g)

            sumLetters = 0
            index = 0
            for c in word:
                if c == g:
                    guessedWord[index * 2] = g
                    sumLetters += 1
                index += 1
            if sumLetters > 1 or sumLetters == 0:
                print("There were " + str(sumLetters) + " " + g + "\'s in the word!")
            else:
                print("There was 1 " + g + " in the word!")
            if sumLetters == 0:
                guessed += 1
            hasGuessed = True

            #check for winner
            if "_" not in guessedWord:
                won = True
                break

        if won:
            print("\nCongratulations! You guessed it! The word was " + word + " and you had " + str(guesses-guessed) + " tries to spare!")
        else:
            print("\nUnfortunately you weren't quick enough. The word was " + word)

        #decide to replay
        print('-'*40)
        replay_answer = input("Would you like to play again? Please respond \"yes\" or \"no\".\n").lower()
        while replay_answer != 'yes' and replay_answer != 'no':
            replay_answer = input('Please respond with \"yes\" or \"no\" only.\n').lower()
        if replay_answer == 'no':
            wants_to_play = False # will be true o/w
        else:
            print('-'*40)
            # print('\n'*3)

if __name__ == '__main__':
    playHangman()

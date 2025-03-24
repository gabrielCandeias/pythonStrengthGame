import random
from os import system, name

# Methods
def clearScreen():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def printStrenght(numberOfTries):

    strenght = [
    '''
        _______
        |     |
        |     0
        |    /|\\
        |     |
        |    / \\
        |
        |
       ---

        ''',
    '''
        _______
        |     |
        |     0
        |    /|\\
        |     |
        |    /
        |
        |
       ---

    ''',
    '''
        _______
        |     |
        |     0
        |    /|\\
        |     |
        |
        |
        |
       ---

    ''',
    '''
        _______
        |     |
        |     0
        |    /|
        |     |
        |
        |
        |
       ---

    ''',
    '''
        _______
        |     |
        |     0
        |     |
        |     |
        |
        |
        |
       ---

    ''',
    '''
        _______
        |     |
        |     0
        |
        |
        |
        |
        |
       ---

    ''',
    '''
        _______
        |     |
        |
        |
        |
        |
        |
        |
       ---

    ''',
    ]

    print(strenght[numberOfTries])

def startGame():
    # The possible challenges is separated in:
    # Themes
    # possible cases on the themes
    posibleChallenges = {
        'food' : [
            'BANANA',
            'BANANA',
            'BANANA',
            'BANANA',
        ],
        'cars' : [
            'MUSTANG',
            'GOL',
            'MUSTANG',
            'COROLLA',
            'FERRARI',
        ]
    }

    while True:
        clearScreen()
        print("============================")
        print("Hello, Welcome to the Game!!")
        print("============================")

        theme = random.choice(list(posibleChallenges.keys()))
        challenge = random.choice(posibleChallenges[theme])
        print("The Theme is: ", theme)

        numberOfTries = 6
        wrongWords = []
        rightWords = ['_' for word in challenge]
        success = False

        while True:

            printStrenght(numberOfTries)
            print('Right Words: ', ' '.join(rightWords))
            print('Wrong Words: ', ' '.join(wrongWords))
            print('Chances: ', numberOfTries)

            currentWord = input('Choice one Word: ').upper()

            if(currentWord in challenge):
                index=0
                for word in challenge:
                    if currentWord == word:
                        rightWords[index] = word
                    index += 1
            else:
                numberOfTries -= 1
                wrongWords.append(currentWord)

            if('_' not in  rightWords):
                print('Congratulations you WIN!!!')
                break
            else:
                if (numberOfTries == 0):
                    print('Unfortunately you use all the chances. The Word is: ', challenge)
                    break

        print('Thanks for play my game. What do you want do now?')
        choice = input(' 1 - Play again \n 2 - Exit \n Choice: ')

        if(choice == '1'):
            continue
        else:
            break

if __name__ == "__main__":
    startGame()

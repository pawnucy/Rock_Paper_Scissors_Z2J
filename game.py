import random

# Beautiful text decoration used in several places ;)
decor = '--------------------------------'


def welcome():
    # Displays information about the game
    print(f'{decor}\n\tROCK / PAPER / SCISSORS\n\t  THE INCREDIBLE GAME\n{decor}')
    main_menu()


def main_menu():
    # The main menu where the player chooses whether to start a new game or quit it.
    print('\nMAIN MENU\n1) New Game\n2) Quit')
    # Checking if the player has entered the correct type of data (only numbers are accepted).
    try:
        player_input = int(input('\nEnter number: '))
    except ValueError:
        print(f'Incorrect data entered, make sure you are entering numbers!\n{decor}')
        main_menu()
    else:
        if player_input == 1:
            # Starting a new game.
            new_game()
        elif player_input == 2:
            # Closing the program.
            print('Meh, you probably have better things to do...')
            quit()
        else:
            print(f'Please enter number 1 or 2.\n{decor}')
            main_menu()


def new_game():
    # Starting a new game.
    print(f'{decor}\n\nTo leave the game type "quit" at any time.'
          f'\nEnter the number of the item you want to use for the fight: ')
    print('1) ROCK    2) PAPER   3) SCISSORS')
    # Enter player choice.
    player_input = input('\n\tCHOICE: ')

    choices = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS'}
    # A random choice for the computer player.
    computer_choice = random.choice(list(choices.keys()))

    if player_input == 'quit':
        # Closing the program.
        print('Meh, you probably have better things to do...')
        quit()
    else:
        # Checking if the player has entered the correct type of data (only numbers are accepted).
        try:
            player_choice = int(player_input)
        except ValueError:
            print(f'Please enter number 1, 2 or 3.')
            new_game()
        else:
            # Displays player and computer choices.
            compare_choices = f'\nYour choice: {choices.get(player_choice)}' \
                              f'\nComputer choice: {choices.get(computer_choice)}'
            # Comparison of choices and display of game results.
            if player_choice < 1 or player_choice > 3:
                print(f'Please enter number 1, 2 or 3.')
                new_game()
            elif player_choice == computer_choice:
                print(f'{compare_choices}\n\n== Draw! There is no winner ==')
            elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or \
                    (player_choice == 3 and computer_choice == 2):
                print(f'{compare_choices}\n\n== Congratulations! YOU WIN! ==')
            else:
                print(f'{compare_choices}\n\n== You Lose! Maybe next time ==')
    new_game()


if __name__ == "__main__":
    welcome()

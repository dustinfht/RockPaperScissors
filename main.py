import random
import configparser

items = {"P": "Paper", "R": "Rock", "S": "Scissor"}
# messages
global draw_message
global won_message
global lost_message
global head_message
global select_message
global unknown_selection_message
global exit_message
global another_game


def load_file():
    configParser = configparser.RawConfigParser()
    configFilePath = r"config.cfg"
    configParser.read(configFilePath)

    global draw_message
    draw_message = configParser.get("messages", "draw")
    global won_message
    won_message = configParser.get("messages", "won")
    global lost_message
    lost_message = configParser.get("messages", "lost")
    global head_message
    head_message = configParser.get("messages", "head")
    global select_message
    select_message = configParser.get("messages", "select_input")
    global unknown_selection_message
    unknown_selection_message = configParser.get("messages", "unknown_selection")
    global exit_message
    exit_message = configParser.get("messages", "exit")
    global another_game
    another_game = configParser.get("messages", "another_game")


def new_round():
    print(another_game)
    another_game_input = input().lower()
    if another_game_input == "y":
        return True
    elif another_game_input == "n":
        return False
    else:
        return new_round()


def get_user_input():
    print(select_message)
    user_input = input().upper()
    if user_input == "exit".upper():
        return user_input
    if not user_input == "exit" and user_input not in items.keys():
        return get_user_input()

    return user_input


def game():
    print(head_message)
    while True:
        user_input = get_user_input()
        if user_input == "EXIT":
            print(exit_message)
            return

        user_selection = items.get(user_input)
        computer_selection = random.choice(list(items.values()))

        if user_selection == computer_selection:
            print(draw_message % user_selection)
        elif user_selection == "Paper":
            if computer_selection == "Rock":
                print(won_message % (user_selection, computer_selection))
            else:
                print(lost_message % (user_selection, computer_selection))
        elif user_selection == "Rock":
            if computer_selection == "Scissor":
                print(won_message % (user_selection, computer_selection))
            else:
                print(lost_message % (user_selection, computer_selection))
        elif user_selection == "Scissor":
            if computer_selection == "Rock":
                print(won_message % (user_selection, computer_selection))
            else:
                print(lost_message % (user_selection, computer_selection))

        new_round_result = new_round()
        if not new_round_result:
            break

    print(exit_message)


if __name__ == '__main__':
    load_file()
    game()

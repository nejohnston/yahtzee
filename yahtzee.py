"""
COMP 1510 - Yahtzee
Nicholas Johnston
A01242666
November 30, 2020
"""
import json
import random
import re


def PLAYER_1_NUMBER():
    return 1


def PLAYER_2_NUMBER():
    return 2


def FULL_HOUSE_SCORE():
    return 25


def SMALL_STRAIGHT_SCORE():
    return 30


def LARGE_STRAIGHT_SCORE():
    return 40


def YAHTZEE_SCORE():
    return 50


def SECOND_YAHTZEE_SCORE():
    return 100


def NO_SCORE():
    return 0


def FIRST_ROLL_COUNT():
    return 3


def LAST_ROLL_COUNT():
    return 1


def ASCII_FILE_PATH():
    return 'ascii_dice.txt'


def SCORECARD_FILE_PATH():
    return 'scorecard.json'


def SCORECARD_TEMPLATE():
    return scorecard_get()


def ascii_get() -> dict:
    """
    Open json scorecard

    :precondition: file location is correct
    :precondition: json is in scorecard format
    :postcondition: dictionary of a score sheet
    :return: dictionary
    """
    with open(ASCII_FILE_PATH()) as fileobject:
        return fileobject.read()


def scorecard_get() -> dict:
    """
    Open json scorecard.

    :precondition: file location is correct
    :precondition: json is in scorecard format
    :postcondition: dictionary of a score sheet
    :return: dictionary
    """
    with open(SCORECARD_FILE_PATH()) as fileobject:
        return json.load(fileobject)


def validate_full_house(dice_list: list) -> int:
    """
    Validate a full house

    :postcondition: integer of small straight score value or no score if not valid
    :return: integer
    >>> validate_full_house([3, 3, 3, 6, 6])
    25
    >>> validate_full_house([1, 1, 1, 1, 2])
    0
    """
    sorted_dice_list = sorted(dice_list)
    first_digit = sorted_dice_list[0]
    second_digit = sorted_dice_list[4]
    count_first_digit = sorted_dice_list.count(first_digit)
    count_last_digit = sorted_dice_list.count(second_digit)
    if (count_first_digit == (2 or 3)) and (count_last_digit == (2 or 3)):
        return FULL_HOUSE_SCORE()
    return NO_SCORE()


def validate_small_straight(dice_list: list) -> int:
    """
    Validate a small straight

    :postcondition: integer of full house score value or no score if not valid
    :return: integer
    >>> validate_small_straight([1, 2, 3, 4, 6])
    30
    >>> validate_small_straight([1, 1, 1, 1, 2])
    0
    """
    dice_str = ''.join(sorted(dice_list))
    small_straight_regex = re.compile(r'1234|2345|3456')
    small_straight_match = small_straight_regex.search(dice_str)
    if small_straight_match:
        return SMALL_STRAIGHT_SCORE()
    else:
        return NO_SCORE()


def validate_large_straight(dice_list: list) -> int:
    """
    Validate a small straight

    :postcondition: integer of small straight score value or no score if not valid
    :return: integer
    >>> validate_large_straight([1, 2, 3, 4, 6])
    30
    >>> validate_large_straight([1, 1, 1, 1, 2])
    0
    """
    dice_list = ''.join(sorted(dice_list))
    large_straight_regex = re.compile(r'12345|23456')
    large_straight_match = large_straight_regex.search(dice_list)
    if large_straight_match:
        return SMALL_STRAIGHT_SCORE()
    else:
        return NO_SCORE()


def validate_yahtzee(dice_list: list) -> int:
    """
    Validate a small straight

    :postcondition: integer of small straight score value or no score if not valid
    :return: integer
    >>> validate_yahtzee([1, 1, 1, 1, 1])
    50
    >>> validate_yahtzee([1, 1, 1, 1, 2])
    0
    """
    first_dice = dice_list[0]
    for dice in dice_list:
        if dice != first_dice:
            return NO_SCORE()
    return YAHTZEE_SCORE()


def scorecard_update(scorecard: dict, player_scorecard_choice: str, score_value: int) -> dict:
    """
    Update scorecard based on player's choice.

    Call scorecard_validate() and determine which to update.

    :param scorecard: dict
    :param player_scorecard_choice: str
    :param score_value: int
    :precondition: scorecard is a valid dict
    :precondition: player_scorecard_choice has been validated
    :precondition: player_scorecard_choice is open on scorecard
    :precondition: player_dice is a list of 5 integers
    :postcondition: dict with updated score values
    """
    print(f'You scored: {score_value}\n')
    for key, value in scorecard.items():
        if key == player_scorecard_choice:
            scorecard[key] = score_value


def scorecard_calculate_upper(player_dice, player_choice_upper) -> int:
    """
    Calculate the score of the upper selection.

    :param player_dice: list of integers
    :param player_choice_upper: string of available upper score
    :precondition: player_choice_upper must be an available score on the scorecard
    :precondition: player_dice is a list of 5 integers
    :postcondition: integer based on the values in the player's dice
    :return: integer

    >>> scorecard_calculate_upper([1, 2, 1, 1, 1], "1")
    4
    >>> scorecard_calculate_upper([1, 2, 1, 1, 1], "2")
    2
    >>> scorecard_calculate_upper([1, 2, 1, 1, 1], "6")
    0
    """
    upper_choice = int(player_choice_upper)
    choice_in_dice = player_dice.count(upper_choice)
    return choice_in_dice * upper_choice


def scorecard_calculate_lower(player_dice, player_choice_lower) -> int:
    """
    Calculate the score of the lower selection.

    :param player_dice: list of integers
    :param player_choice_lower: string of available lower score
    :precondition: player_choice_lower must be an available score on the scorecard
    :precondition: player_dice is a list of 5 integers
    :postcondition: integer based on the values in the player's dice
    :return: integer

    >>> scorecard_calculate_upper([1, 2, 3, 4, 1], "small straight")
    30
    >>> scorecard_calculate_upper([1, 2, 3, 4, 5], "large straight")
    40
    >>> scorecard_calculate_upper([1, 2, 1, 1, 1], "4 of a kind")
    6
    """
    pass


def handle_validation(player_scorecard_choice, player_dice, player_scorecard) -> bool:
    """
    Determine if the player's dice and their chosen score are valid.

    :param player_scorecard_choice: string
    :param player_dice: list of integers
    :param player_scorecard: dict
    :precondition: player_dice must be a list of 5 integers
    :postcondition: boolean based on if the choice is valid
    :return: boolean

    >>> handle_validation("small straight", [1,2,3,4,6])
    True
    >>> handle_validation("yahtzee", [1,2,3,4,5])
    False
    """
    validation = False
    if player_scorecard_choice in upper_keys():
        lower_score = scorecard_calculate_upper(player_dice, player_scorecard_choice)
        scorecard_update(player_scorecard['scorecard']['upper'], player_scorecard_choice, lower_score)
    if player_scorecard_choice in lower_keys():
        if player_scorecard_choice == 'smallstraight':
            validation = validate_small_straight(player_dice)
        if player_scorecard_choice == 'largestraight':
            validation = validate_large_straight(player_dice)
        if player_scorecard_choice == 'fullhouse':
            validation = validate_full_house(player_dice)
        if player_scorecard_choice == 'yahtzee':
            validation = validate_yahtzee(player_dice)
        if player_scorecard_choice == 'chance':
            validation = sum(player_dice)
        scorecard_update(player_scorecard['scorecard']['lower'], player_scorecard_choice, validation)
    return validation


def calculate_total_upper(scorecard):
    """
    Calculate the total current score
    :return:
    """
    score = 0
    for value in scorecard['scorecard']['upper'].values():
        if value:
            score += value
    return score


def calculate_total_lower(scorecard):
    """
    Calculate the total current score
    :return:
    """
    score = 0
    for value in scorecard['scorecard']['lower'].values():
        if value:
            score += value
    return score


def upper_keys():
    """
    Find all the keys from the scorecard

    :return: list
    """
    scorecard = SCORECARD_TEMPLATE()
    keys_list = [key for key in scorecard['scorecard']['upper']]
    return keys_list


def lower_keys():
    """
    Find all the keys from the scorecard

    :return: list
    """
    scorecard = SCORECARD_TEMPLATE()
    keys_list = [key for key in scorecard['scorecard']['lower']]
    return keys_list


def scorecard_format(scorecard) -> print:
    """
    Format scorecard for player.

    :param scorecard: dict
    :precondition: scorecard is a valid dictionary scorecard
    :postcondition: print available scores for player one

    >>> scorecard_format({"upper": {"1": -1, "2": -1, "3": -1, "4": -1, "5": -1, "6": -1}, \
                            "lower": {"3_kind": -1, "4_kind": -1,"full_house": -1, "small_straight": -1, \
                                        "large_straight": -1, "yahtzee": -1, "chance": -1}})
    Player One Scorecard:
    Upper:
        1:
        2:
        3:
        4:
        5:
        6:
    Total Score:
    Bonus:
    Total of Upper Section:

    Lower:
        3 of a Kind:
        4 of a Kind:
        Full House:
        Small Straight:
        Large Straight:
        Yahtzee:
        Chance:
    Total Score:
    Bonus:
    Total of Upper Section:
    Total of Lower Section:

    Grand Total:
    >>> scorecard_format({"upper": {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6}, \
                            "lower": {"3_kind": False, "4_kind": False,"full_house": False, "small_straight": False, \
                                        "large_straight": False, "yahtzee": False, "chance": False}})
    Player One Scorecard:
    Upper:
        1:    1
        2:    2
        3:    3
        4:    4
        5:    5
        6:    6
    Total Score: 21
    Bonus: 0
    Total of Upper Section: 21

    Lower:
        3 of a Kind:
        4 of a Kind:
        Full House:
        Small Straight:
        Large Straight:
        Yahtzee:
        Chance:
    Total Score:
    Bonus:
    Total of Upper Section:
    Total of Lower Section:

    Grand Total:

    """
    print('Upper:')
    for key, value in scorecard['scorecard']['upper'].items():
        if not value or value == 0:
            print(f"{key}:")
    print('\nLower:')
    for key, value in scorecard['scorecard']['lower'].items():
        if not value or value == 0:
            print(f'{key}: ')


def dice_roll(number_of_dice_to_re_roll) -> list:
    """
    Produce 5 random numbers for the player's initial roll.

    :postcondition: list of random integers
    :return: list

    >>> player_dice_roll(5)
    [1, 2, 3, 4, 5]
    >>> player_dice_roll(4)
    [6, 2, 2, 3]
    >>> player_dice_roll(1)
    [5]
    """
    return [random.randint(1, 6) for _ in range(0, number_of_dice_to_re_roll)]


def format_dice_to_keep_input(player_input: str) -> list:
    """
    Format player input indicating dice to re roll

    :param player_input: string
    :postcondition: list of index of dice to keep
    :return list
    """
    try:
        indices_to_input = player_input.split(' ')
        player_input_int = list(map(int, indices_to_input))
        return player_input_int
    except ValueError:
        print('You have entered an incorrect value')


def update_dice_from_roll(original_roll: list, dice_to_remove: list) -> list:
    """
    Update indicated dice from original_roll

    :param original_roll: list
    :param dice_to_remove: list
    :postcondition: list of updated roll with the dice user wants to keep
    :return: list
    """
    for dice in range(len(original_roll) + 1):
        if dice in dice_to_remove:
            original_roll[dice - 1] = random.randint(1, 6)
    return original_roll


def handle_dice_roll():
    """
    Handle player dice roll

    Present initial dice roll, determine which dice the player would like to re-roll
    :return:
    """
    roll_count = FIRST_ROLL_COUNT()
    player_dice_roll = dice_roll(5)
    while True:
        print('This is your roll:\n', player_dice_roll)
        player_dice = input("Which dice would you like to re-roll, enter in the dice place separated by a space \n"
                            "If you would like to keep your dice and end your turn press enter")

        roll_count -= 1

        if player_dice == '':
            break

        if roll_count == 0:
            break

        if LAST_ROLL_COUNT() <= roll_count < FIRST_ROLL_COUNT():
            player_dice_roll = update_dice_from_roll(player_dice_roll, format_dice_to_keep_input(player_dice))

    return player_dice_roll


def pass_turn_ownership(previous_player: int) -> int:
    """
    Identify next player
    
    :param previous_player: integer
    :postcondition: integer indicating the next player
    :return: integer
    >>> pass_turn_ownership(1)
    2
    >>> pass_turn_ownership(2)
    1
    """
    if previous_player == 2:
        return PLAYER_1_NUMBER()
    else:
        return PLAYER_2_NUMBER()


def update_player_turn_count(scorecard: int) -> int:
    """
    Update player turn count on scorecard

    :param scorecard:
    :postcondition: scorecard dict with updated turn count
    :return: int
    >>> update_player_turn_count(13)
    12
    >>> update_player_turn_count(8)
    7
    """
    scorecard -= 1
    return scorecard


def turn_operator(turn, scorecard):
    """
    Handle each turn.

    This function will do all the necessary scorecard checks and play through the
    player's dice roll.
    """
    score_dialogue = 'Which score would you like to use?\n' \
                     f'Please enter your choice exactly as it appears on the scorecard, or else!'
    while True:
        resulting_roll = handle_dice_roll()
        print(f'Player {turn} Dice: ', resulting_roll)
        print(f'Player {turn} Scorecard:\n')
        scorecard_format(scorecard)
        score_to_keep = input(score_dialogue).lower()
        handle_validation(score_to_keep, resulting_roll, scorecard)
        scorecard_format(scorecard)
        print('Your upper total is: ', calculate_total_upper(scorecard))
        print('Your lower total is: ', calculate_total_lower(scorecard))
        print('Your grand total is: ', calculate_total_upper(scorecard) + calculate_total_lower(scorecard))
        return False


def game():
    """
    Drive the game.

    Control the amount of turns and hold onto a consistent version of the scorecard
    """
    player_1_scorecard = SCORECARD_TEMPLATE()
    player_2_scorecard = SCORECARD_TEMPLATE()
    turn = PLAYER_1_NUMBER()
    print('Welcome to Yahtzee!')
    input('Press enter to start your game :)')
    while True:
        if turn == PLAYER_1_NUMBER():
            input(f'Player {turn}, it is your turn. Press any key to roll :)')
            turn_operator(turn, player_1_scorecard)
            update_player_turn_count(player_1_scorecard['turn'])
        if turn == PLAYER_2_NUMBER():
            input(f'Player {turn}, it is your turn. Press any key to roll :)')
            turn_operator(turn, player_2_scorecard)
            update_player_turn_count(player_2_scorecard['turn'])
        turn = pass_turn_ownership(turn)


def main():
    """
    Drives the function.
    """
    game()


if __name__ == "__main__":
    main()

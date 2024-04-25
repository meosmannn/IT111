def dice_game():
    turn_number = 1
    point_number = None

    while True:
        die_roll = int(input("Enter die roll (2-12): "))
        if die_roll < 2 or die_roll > 12:
            raise ValueError("Die roll must be a number from 2 to 12.")

        if turn_number == 1 and die_roll in [2, 3, 12]:
            return f"Turn: {turn_number}, Die Roll: {die_roll}, Result: Player loses"
        elif turn_number == 1 and die_roll in [7, 11]:
            return f"Turn: {turn_number}, Die Roll: {die_roll}, Result: Player wins"
        elif die_roll == 7:
            return f"Turn: {turn_number}, Die Roll: {die_roll}, Result: Player loses"
        elif die_roll == point_number:
            return f"Turn: {turn_number}, Die Roll: {die_roll}, Result: Player wins"

        point_number = point_number or die_roll
        turn_number += 1
        print(f"Turn: {turn_number}, Die Roll: {die_roll}, Result: Continue game")

print(dice_game())

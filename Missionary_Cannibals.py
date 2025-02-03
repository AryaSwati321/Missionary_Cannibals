from IPython.display import clear_output

boat_side = 'Right'
missionaries_on_right = 3
cannibals_on_right = 3
missionaries_on_left = 0
cannibals_on_left = 0

def display_status():
    print("Left Bank: ", '\U0001f482'*missionaries_on_left, '\U0001f479'*cannibals_on_left)
    print("Boat: ", '\U0001f6A2' if boat_side == 'Right' else '', " \U0001f6A2" if boat_side == 'Left' else '')
    print("Right Bank: ", '\U0001f482'*missionaries_on_right, '\U0001f479'*cannibals_on_right)
    print('\U0001f30a'*8)  # River representation

clear_output()
display_status()

while True:
    print(f"\nBoat is on the {boat_side} side.")
    
    missionaries = int(input('ENTER THE NUMBER OF MISSIONARIES ON BOAT (0-2): '))
    cannibals = int(input('ENTER THE NUMBER OF CANNIBALS ON BOAT (0-2): '))

    if (missionaries + cannibals) < 1 or (missionaries + cannibals) > 2:
        print("Invalid Move: The boat must carry 1 or 2 people!")
        continue

    if boat_side == 'Right':
        if missionaries > missionaries_on_right or cannibals > cannibals_on_right:
            print("Invalid Move: Not enough people on the right bank!")
            continue
        else:
            missionaries_on_right -= missionaries
            cannibals_on_right -= cannibals
            missionaries_on_left += missionaries
            cannibals_on_left += cannibals
            boat_side = 'Left'

    elif boat_side == 'Left':
        if missionaries > missionaries_on_left or cannibals > cannibals_on_left:
            print("Invalid Move: Not enough people on the left bank!")
            continue
        else:
            missionaries_on_left -= missionaries
            cannibals_on_left -= cannibals
            missionaries_on_right += missionaries
            cannibals_on_right += cannibals
            boat_side = 'Right'

    clear_output()
    display_status()

    if (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) or \
       (missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):
        print("YOU LOSE! The cannibals outnumbered the missionaries.")
        break

    if missionaries_on_left == 3 and cannibals_on_left == 3:
        print("CONGRATULATIONS! YOU WIN! Everyone is safely across.")
        break

print("GAME OVER")

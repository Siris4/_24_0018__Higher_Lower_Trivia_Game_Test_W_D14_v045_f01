import random
from _24_0018__D14_v01_f01_Higher_Lower_Trivia_Game_logo_W import logo, vs
from _24_0018__D14_v00_f01_Higher_Lower_Trivia_Game_gamedata_W import data

print(logo)

counter = 1
previous_index_holder = 0

profile_A = None
profile_B = None
random_profile_index_number_picked_B = 0

def game_on():
    global counter, profile_A, profile_B
    score = 0

    while True:
        if counter >= 2:
            profile_a = profile_b
            profile_b = data[random_profile_index_number_picked_B]
        else:
            global previous_index_holder
            random_profile_index_number_picked_A = random.randrange(0, 50)
            profile_a = data[random_profile_index_number_picked_A]
            print(f'The number was {random_profile_index_number_picked_A}')
            print(f"The profile number that was chosen is index #: {random_profile_index_number_picked_A}")
            profile_b = None

        counter += 1
        profile_name_A = profile_a.get('name')
        print(profile_name_A)
        hidden_profile_A_follower_count = profile_a.get('follower_count')

        print(vs)

        # random_profile_index_number_picked_B  #was global before
        random_profile_index_number_picked_B = random.randrange(0, 50)
        while random_profile_index_number_picked_B == random_profile_index_number_picked_A:
            random_profile_index_number_picked_B = random.randrange(0, 50)

        profile_b = data[random_profile_index_number_picked_B]
        print(f"The profile number that was chosen is index #: {random_profile_index_number_picked_B}")
        previous_index_holder += random_profile_index_number_picked_B
        profile_name_B = profile_b.get('name')
        print(profile_name_B)
        hidden_profile_B_follower_count = profile_b.get('follower_count')

        a_or_b_profile_user_pick = input(f"Do you think that A or B has more followers? (A or B): ").upper()
        if hidden_profile_A_follower_count > hidden_profile_B_follower_count and a_or_b_profile_user_pick == "A":
            print(f"Yay!! You got it right! {profile_name_A} has {hidden_profile_A_follower_count} million subscribers.")
        elif hidden_profile_A_follower_count < hidden_profile_B_follower_count and a_or_b_profile_user_pick == "B":
            print(f"Yay!! You got it right! {profile_name_B} has {hidden_profile_B_follower_count} million subscribers.")
        else:
            print(f"Sorry, but you failed. {profile_name_A} has {hidden_profile_A_follower_count} million subscribers, and {profile_name_B} has {hidden_profile_B_follower_count} million subscribers.")
            game_on = False

        continue_next_part = input("Shall we continue? (Y or N): ").upper()
        if continue_next_part == "Y":
            game_on = True
        else:
            print("OK then, good day to you too sir")
            return False

game_on()

play_again_option = input("Do you want to play again? (Y or N): ").upper()
if play_again_option == "Y":
    game_on()

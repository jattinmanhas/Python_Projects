import random

choice = input("What's your choice? 'r' for Rock, 'p' for Paper and 's' for Scissor: ").lower()
comp_choice = random.choice(['r','p','s'])

def rps_game(choice , comp_choice):
    if(choice == comp_choice):
        return ("It's a tie.")
    
    if is_win(choice, comp_choice):
        return "You win"
    
    return "You loose"

def is_win(choice, comp_choice):
    if ((choice == 'r' and comp_choice=='s') or (choice== 's' and comp_choice == 'p') or (choice == 'p' and  comp_choice == 'r')):
        return True
    else:
        return False

print(rps_game(choice, comp_choice))

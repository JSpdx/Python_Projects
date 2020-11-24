import random

if __name__ == "__main__":

    game_in_action = True
    hands = {1 : 'Rock', 2: 'Paper', 3: 'Scissors'}
    print('Let\'s play rock paper scissors')
    while game_in_action:
        player_throw = int(input('Type 1 for rock, 2 for paper, or 3 for scissors: '))
        
        npc_throw = random.randint(1, 3)
        print("The computer threw {}".format(hands[npc_throw]))
        print("You threw {}".format(hands[player_throw]))
        
        if player_throw == npc_throw:
            print('Draw. Throw again.')  
        elif player_throw == 1 and npc_throw == 2:
            
    
  
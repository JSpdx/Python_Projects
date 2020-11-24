import random

def game_logic(player_throw, npc_throw, ):
            if player_throw == npc_throw:
                print('Draw. Throw again.')
            elif player_throw == 1 and npc_throw == 2:
                print("Paper beats rock, one point to computer.")
                score['npc'] += 1
            elif player_throw == 1 and npc_throw == 3:
                print('Rock crushes scissors, one point to you.')
                score['player'] += 1
            elif player_throw == 2 and npc_throw == 1:
                print('Paper covers rock, one point to you.')
                score['player'] += 1
            elif player_throw == 2 and npc_throw == 3:
                print('Scissors cut paper, one point to computer.')
                score['npc'] += 1
            elif player_throw == 3 and npc_throw == 1:
                print('Rock crushes scissors, one point to computer.')
                score['npc'] += 1
            elif player_throw == 3 and npc_throw == 2:
                print('Scissors cut paper, one point to you.')
                score['player'] += 1
            return

def reset_score(score):
    for k, v in score.items():
       score[k] = 0
    return 



if __name__ == "__main__":

    game_in_action = True
    hands = {1 : 'Rock', 2: 'Paper', 3: 'Scissors'}
    score = {'player': 0, 'npc': 0}
    print('Let\'s play rock paper scissors. First to 3 wins!')
    while game_in_action: 
        npc_throw = random.randint(1, 3)
        player_throw = int(input('Type 1 for rock, 2 for paper, or 3 for scissors: '))
        while True:
            if player_throw >= 1 and player_throw <= 3:
                break
            else:
                player_throw = int(input('Sorry that was an invalid number. \n Type 1 for rock, 2 for paper, or 3 for scissors:  '))
        print("You threw {}".format(hands[player_throw]))
        print("The computer threw {}".format(hands[npc_throw]))
        game_logic(player_throw, npc_throw)
        if score['player'] == 3:
            reset_score(score)
            print('the reset score is {}'.format(score))
            input('You win! Play again? y or n: ')
        if score['npc'] == 3:
            reset_score(score)
            print('the reset score is {}'.format(score))
            input('You lose! Play again? y or n: ')
        
        
        
        
        
        
        
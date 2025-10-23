from utils import deck

def create_player(*name:str):
    player_name = name
    if len(name) == 0:
        player_name = 'AI'
    player = {'name': player_name,'hand':[],'won_pile':[]}
    return player



def init_game():
    player_1 = create_player('yosef')
    player_2 = create_player()
    new_deck = deck.shuffle(deck.create_deck())
    player_1['hand'] = new_deck[0:26]
    player_2['hand'] = new_deck[26:]
    return {'dect':new_deck,
            'player_1':player_1,
            'player_2':player_2}

def play_round(p1:dict,p2:dict):
    if len(p1['hand']) == 0 or len(p1['hand']) == 0:
        print('game over')
        if len(p1['hand']) > 0:
            print('player 1 won')
            return
        elif len(p2['hand']) > 0:
            print('player 2 won')
            return
        elif len(p1['hand']) == 0 and len(p2['hand']) == 0:
            print('Its a draw')
            return
    else:
        hand_1 = p1['hand'].pop()
        hand_2 = p2['hand'].pop()
        if hand_1['value'] > hand_2['value']:
                p1['won_pile'].append(hand_1)
                p1['won_pile'].append(hand_2)
                print('hand 1 won!!!')
        elif hand_1['value'] == hand_2['value']:
            print('Its a draw')
        else:
            p2['won_pile'].append(hand_1)
            p2['won_pile'].append(hand_2)
            print('hand 2 won!!!')









def create_card(rank:str,suite:str):
    upper_case_rank = rank.upper()
    upper_case_suite = suite.upper()
    rele_valyo = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
    card = {'rank':upper_case_rank,'suite':upper_case_suite,'value':rele_valyo[upper_case_rank]}
    return card
#print(create_card('','h'))

def compare_cards(p1_card:dict, p2_card:dict):
    player = p1_card['value']
    player_ai = p2_card['value']
    if player > player_ai:
        return 'p1'
    elif player < player_ai:
        return 'p2'
    elif player == player_ai:
        return 'WAR'

def create_deck():
    rank = ['A','D','C','H']
    list_card = []
    for suit in rank:
        for j in range(2,15):
            if j <= 10:
                list_card.append(create_card(str(j),suit))
            else:
                if j == 11:
                    list_card.append(create_card('J',suit))
                elif j == 12:
                    list_card.append(create_card('Q',suit))
                elif j == 13:
                    list_card.append(create_card('K',suit))
                elif j == 14:
                    list_card.append(create_card('A',suit))
    return list_card


def shuffle(deck:list[dict]):
    import random
    a_mixed_bag = deck
    for i in range(1000):
        random_number1 = random.randint(0,51)
        random_number2 = random.randint(0,51)
        if random_number1 == random_number2:
            continue
        else:
            a_mixed_bag[random_number1], a_mixed_bag[random_number2] = a_mixed_bag[random_number2], a_mixed_bag[random_number1]

    return a_mixed_bag


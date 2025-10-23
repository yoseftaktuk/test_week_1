from game_logic import game
if __name__ == "__main__":
    from  game_logic import game

    a = game.create_player('yosef')
    b = game.init_game()
    c = game.init_game()
    if len(c['player_1']['hand']) or len(c['player_2']['hand']) == 0:
        print('game over')
    else:
        game.play_round(c['player_1'],c['player_2'])
        game.play_round(c['player_1'],c['player_2'])
        game.play_round(c['player_1'],c['player_2'])
        game.play_round(c['player_1'],c['player_2'])
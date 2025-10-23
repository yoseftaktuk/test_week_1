from game_logic import game
if __name__ == "__main__":
    from  game_logic import game

    a = game.create_player('yosef')
    b = game.init_game()
    c = game.init_game()

    game.play_round(c['player_1'],c['player_2'])
    game.play_round(c['player_1'],c['player_2'])
    game.play_round(c['player_1'],c['player_2'])
    game.play_round(c['player_1'],c['player_2'])


from game import GameBase, Game

gb = GameBase()

left = {
    "name": "ku e",
    'pets':[{
        'id': 'bug',
        'level': 69
    }]
}

right = {
    'name': "e ku",
    'pets':[{
        'id': 'bug',
        'level': 96
    }]
}

game = Game(gb, left, right)
game.start_game()
print(game.turns)
print(game.winner)
print(game.winner_content)

class Entities:
    def __init__(self):
        self.snakes = {}    # Dictionary for snakes (start → end)
        self.ladders = {}   # Dictionary for ladders (start → end)
        self.players = {}   # Dictionary for players (index → name)

    def set_snake(self, start_position, end_position):
        self.snakes[start_position] = end_position

    def set_ladder(self, start_position, end_position):
        self.ladders[start_position] = end_position

    def set_player(self, index, player_name):
        self.players[index] = player_name

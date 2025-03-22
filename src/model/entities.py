class Entities:
    _instance = None

    def __init__(self):
        if not hasattr(self, 'snakes'):
            self.snakes = {}
            self.ladders = {}
            self.players = {}

        def set_snake(self, start_position, end_position):
            self.snakes[start_position] = end_position

        def get_snakes(self):
            return self.snakes
        
        def set_ladder(self, start_position, end_position):
            self.ladders[start_position] = end_position

        def get_ladder(self):
            return self.ladders
        
        def set_player(self, index, player_name):
            self.players[index] = player_name

        def get_players(self):
            return self.players
        
        @classmethod
        def get_instance(cls):
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance
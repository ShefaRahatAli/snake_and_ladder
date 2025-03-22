import random

class Dice:
    def __init__(self, number_of_dice=1):
        self.number_of_dice = number_of_dice

    def roll(self):
        return random.randint(1, 6 * self.number_of_dice)  # Assuming a standard dice range


class PlaySnakeAndLadder:
    def __init__(self, num_dice):
        self.player_history = {}
        self.player_latest_position = {}
        self.entities = Entities.get_instance()
        self.dice = Dice(num_dice)

    def play_game(self):
        self.initialize_players_start_value()
        i = -1

        while True:
            i = (i + 1) % len(self.entities.players)
            player_name = self.entities.players[i]
            dice_number = self.dice.roll()
            end_position = self.player_latest_position[player_name] + dice_number
            message = f"{player_name} rolled a {dice_number} and moved from {self.player_latest_position[player_name]}"

            if self.check_for_dice_number_greater_than_100(end_position):
                if end_position in self.entities.snakes:
                    end_position = self.entities.snakes[end_position]
                    message += f" to {end_position} after Snake bite"
                elif end_position in self.entities.ladders:
                    end_position = self.entities.ladders[end_position]
                    message += f" to {end_position} after Ladder climb"
                else:
                    message += f" to {end_position}"

                self.player_latest_position[player_name] = end_position
                print(message)

                if self.is_player_won(player_name):
                    return f"{player_name} wins!"

    def is_player_won(self, player):
        return self.player_latest_position[player] == 100

    def check_for_dice_number_greater_than_100(self, end_position):
        return end_position <= 100

    def initialize_players_start_value(self):
        for player_name in self.entities.players.values():
            self.player_latest_position[player_name] = 0


# Singleton class for game entities
class Entities:
    _instance = None

    def __init__(self):
        self.snakes = {}
        self.ladders = {}
        self.players = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def set_snake(self, start, end):
        self.snakes[start] = end

    def set_ladder(self, start, end):
        self.ladders[start] = end

    def set_player(self, index, name):
        self.players[index] = name


# Example Usage
if __name__ == "__main__":
    entities = Entities.get_instance()
    entities.set_snake(99, 10)
    entities.set_ladder(5, 50)
    entities.set_player(0, "Alice")
    entities.set_player(1, "Bob")

    game = PlaySnakeAndLadder(1)
    winner = game.play_game()
    print(winner)

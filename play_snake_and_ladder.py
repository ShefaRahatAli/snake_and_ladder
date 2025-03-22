import random
from entities import Entities  # Ensure correct import

class PlaySnakeAndLadder:
    def __init__(self, dice_sides=6):
        self.entities = Entities()  # Instance of Entities
        self.dice_sides = dice_sides
        self.player_positions = {}  # Track player positions

    def roll_dice(self):
        return random.randint(1, self.dice_sides)

    def play_game(self):
        for index, player_name in self.entities.players.items():
            self.player_positions[player_name] = 0  # Start at 0

        while True:
            for index, player_name in self.entities.players.items():
                dice_value = self.roll_dice()
                new_position = self.player_positions[player_name] + dice_value

                if new_position > 100:  # Ignore if exceeding 100
                    continue

                # Check snakes and ladders
                if new_position in self.entities.snakes:
                    new_position = self.entities.snakes[new_position]
                    print(f"{player_name} rolled {dice_value} and got bitten by a snake! Moves to {new_position}")
                elif new_position in self.entities.ladders:
                    new_position = self.entities.ladders[new_position]
                    print(f"{player_name} rolled {dice_value} and climbed a ladder! Moves to {new_position}")
                else:
                    print(f"{player_name} rolled {dice_value} and moves to {new_position}")

                self.player_positions[player_name] = new_position

                if new_position == 100:
                    print(f"🎉 {player_name} wins the game! 🎉")
                    return player_name  # End game

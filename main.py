from entities import Entities
from play_snake_and_ladder import PlaySnakeAndLadder

def main():
    entities = Entities()

    # Input Snakes
    num_snakes = int(input("Enter number of snakes: "))
    for _ in range(num_snakes):
        start, end = map(int, input("Enter snake start and end: ").split())
        entities.set_snake(start, end)

    # Input Ladders
    num_ladders = int(input("Enter number of ladders: "))
    for _ in range(num_ladders):
        start, end = map(int, input("Enter ladder start and end: ").split())
        entities.set_ladder(start, end)

    # Input Players
    num_players = int(input("Enter number of players: "))
    for i in range(num_players):
        player_name = input(f"Enter name of player {i+1}: ")
        entities.set_player(i, player_name)

    # Start the game
    game = PlaySnakeAndLadder()
    winner = game.play_game()
    print(f"\n🏆 {winner} is the winner! 🏆")

if __name__ == "__main__":
    main()

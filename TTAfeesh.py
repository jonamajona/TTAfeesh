from enum import Enum  # TODO can't figure out where this is used - remove if not required
# TODO only import those classes that are being used in this main doc (call it main.py?)
import gameClass as Game
import playerClass as Player
import deckClass as Deck

players = int(input("How many players? "))
while players != 2 and players != 3 and players != 4:
    players = int(input("Please select 2, 3 or 4 players: "))
print(f"There are {players} players\n")

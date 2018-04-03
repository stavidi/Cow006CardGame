from witch_game import WitchGame
from witch_player import WitchHuman, WitchRandomComputer
"""MAIN FILE"""
if __name__ == "__main__":
  WitchGame([
    WitchRandomComputer("Alice"),
    WitchRandomComputer("Bob"),
    WitchRandomComputer("Carol"),
    WitchRandomComputer("Dave")
  ]).play()

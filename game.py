from player import Player
from phase import Phase

from singleton import Singleton

class Game(object):
  __metaclass__ = Singleton
  def __init__(self, players, phase):
    self.players = players
    self.current_player = players[0]
    self.phase = phase
    self.winner = None
    self.loser = None

  def next_player(self):
    self.current_player = self.players[1]
    self.players = self.players[1:] + self.players[:1]

  def start(self):
    pass

  def play(self):
    self.start()
    while True:
      self.phase()()
      if self.loser:
        print ("Player %s has lost a game" % self.loser.name)
        break
      if self.winner:
        print("%s has won!" % self.winner.name)
        break
      self.next_player()

  def __repr__(self):
    ret = ""
    for player in self.players:
      ret = ret + repr(player)
    return ret

  def __str__(self):
    ret = ""
    for player in self.players:
      ret = ret + str(player)
    return ret


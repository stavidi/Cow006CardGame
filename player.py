class Player(object):
  def __init__(self, name):
    self.name = name
  def __eq__(self, other):
    return self.name == other.name
  def __nq__(self, other):
    return self.name != other.name
  def __str__(self):
    return "Player %s" % (self.name)
  def __repr__(self):
    return "Player %s" % (self.name)

class Computer(Player):
  pass

class Human(Player):
  pass

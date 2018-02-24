class Card(object):
  @staticmethod
  def all_cards():
    raise NotImplementedError
  def __init__(self):
    pass
  def __eq__(self, other):
    raise NotImplementedError
  def __ne__(self, other):
    return not (self == other)
  def __repr__(self):
      return "Card"
  def __str__(self):
      return "Card"

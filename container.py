import random

from card import Card

class Container(object):
  def __init__(self):
    self.cards = []

  def add_card(self, card):
    if not isinstance(card, Card):
      raise Exception("Trying to add class %s to %s" % (type(card), self.__class__.__name__))
    self.cards.append(card)

  def draw(self):
    return self.cards.pop()

  def discard(self, card = None, top = False):
    if card is None:
      if top == False:
        return self.pop(random.choice(self.cards))
      else:
        return self.draw()
    else:
      self.remove(card)
      return card

  def shuffle(self):
    random.shuffle(self.cards)
    return self

  def __getattr__(self, name):
    return self.cards.__getattribute__(name)

  def __len__(self):
    return len(self.cards)

  def __getitem__(self, pos):
    return self.cards[pos]

  def __str__(self):
    return "%s with %d cards" % (self.__class__.__name__, len(self))

  def __repr__(self):
    r = str(self) + "\n"
    for c in self.cards:
      r+= "  %s\n" % repr(c)
    return r


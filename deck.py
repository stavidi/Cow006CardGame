from card import Card
from container import Container

class Deck(Container):
  @classmethod
  def full_deck(cls, card, player = None):
    d = cls()
    if player:
      all_cards = card.all_cards(player)
    else:
      all_cards = card.all_cards()
    for c in all_cards:
        d.add_card(c)
    return d

class ReshuflableDeck(Deck):
  def __init__(self):
    self.discard = Container()
    super(ReshuflableDeck, self).__init__()

  def draw(self):
    if len(self.cards) > 0:
      return self.cards.pop()
    elif len(self.discard.cards) > 0:
      self.cards = self.discard.cards
      self.shuffle()
      self.discard = Container()
      return self.cards.pop()
    else:
      raise Exception("Can not draw from empty deck without discard")

  def bury(self, card):
    self.discard.add_card(card)

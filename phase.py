class Phase(object):
  __hooks = []

  def __init__(self):
    pass

  @staticmethod
  def add_hook(hook):
    __hooks.append(hook)

  @staticmethod
  def remove_hook(hook):
    #TODO: check if safe
    __hooks.remove(hook)

  def __call__(self):
    self.play()

  def play(self):
    raise NotImplementedError

  def __str__(self):
    return self.__class__.__name__

  def __repr__(self):
    return str(self)

def HookablePhase(Phase):
  __hooks = []

  @staticmethod
  def add_hook(hook):
    __hooks.append(hook)

  @staticmethod
  def remove_hook(hook):
    #TODO: check if safe
    __hooks.remove(hook)

  def __call__(self):
    self.play()
    self.end()

  def play(self):
    raise NotImplementedError

  def end(self):
    for h in self.__hooks:
      h()()

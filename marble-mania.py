class Marble_Game:
  center_marbles = []
  marble_value = 0
  current_marble = 0
  def __init__(self, player_count, marble_count):
    self.player_scores = [0] * player_count
    self.marble_count = marble_count
  def play(self):
    if self.marble_count == 0:
      return self.player_scores
    self.marble_count -= 1
    if len(self.center_marbles) == 0:
      self.center_marbles.append(self.marble_value)
      self.current_marble = 0
    elif len(self.center_marbles) == 1:
      self.center_marbles.append(self.marble_value)
      self.current_marble = 1
    elif len(self.center_marbles) == 2:
      self.center_marbles.insert(1, self.marble_value)
      self.current_marble = 1
    elif len(self.center_marbles) > 2:
      if self.current_marble + 2 > len(self.center_marbles):
        self.current_marble -= (len(self.center_marbles))
      self.center_marbles.insert(self.current_marble + 2, self.marble_value)
      self.current_marble += 2

    self.marble_value += 1
    print(self.current_marble, ' ', self.center_marbles)
    self.play()
test = Marble_Game(9,25)
test.play()


# Jasper Shangle - ChiPy Challenge for January 17, 2019
class Marble_Game:
  center_marbles = []
  marble_value = 0
  current_marble = 0
  whos_turn = 0
  def __init__(self, player_count, marble_count):
    self.player_scores = [0] * player_count
    self.marble_count = marble_count
    self.player_count = player_count
  def play(self):
    while self.marble_count > 0:
      # is current marble a multiple of 23?
      if self.marble_value % 23 == 0 and self.marble_value != 0:
        self.player_scores[self.whos_turn] += self.marble_value
        if self.current_marble - 7 < 0:
          self.current_marble += len(self.center_marbles)
        self.current_marble -= 7
        self.player_scores[self.whos_turn] += self.center_marbles[self.current_marble]
        self.center_marbles.pop(self.current_marble)

      # first three marbles:
      elif len(self.center_marbles) == 0:
        self.center_marbles.append(self.marble_value)
        self.current_marble = 0
      elif len(self.center_marbles) == 1:
        self.center_marbles.append(self.marble_value)
        self.current_marble = 1
      elif len(self.center_marbles) == 2:
        self.center_marbles.insert(1, self.marble_value)
        self.current_marble = 1

      # all other marbles
      elif len(self.center_marbles) > 2:
        if self.current_marble + 2 > len(self.center_marbles):
          self.current_marble -= (len(self.center_marbles))
        self.center_marbles.insert(self.current_marble + 2, self.marble_value)
        self.current_marble += 2

      # set next players turn
      if self.whos_turn < self.player_count - 1:
        self.whos_turn += 1
      else:
        self.whos_turn = 0

      # increase marble value for next marble and go to next turn
      self.marble_value += 1
      # remove marble in play for this turn
      self.marble_count -= 1

    print(self.player_count, max(self.player_scores))
    # print(f"Gameover! There were {self.player_count} players. Below are their scores: ")
    # for index, score in enumerate(self.player_scores):
    #   print(f"Player {index}: {score}")

test = Marble_Game(9,25)
test.play()
test = Marble_Game(10,1618) # 8317
test.play()
test = Marble_Game(13,7999) # 146373
test.play()
test = Marble_Game(17,1104) # 2764
test.play()
test = Marble_Game(21,6111) # 54718
test.play()
test = Marble_Game(30,5807) # 37305
test.play()



import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs) :
    self.items    = kwargs.items()
    self.balls    = [ key for (key,val) in kwargs.items() ]
    self.numbers  = [ val for (key,val) in kwargs.items() ]
    self.contents = []
    for i in range(len(self.balls)) :
      for j in range(self.numbers[i]) : self.contents.append(self.balls[i])
    self.ball_draw = []
 
  def draw(self, num = 0) :
    len_contents  = len(self.contents)
    for i in range(len_contents) :
      len_ball_draw = len(self.ball_draw)
      random.shuffle(self.contents)
      rand_ball = random.randint(0, len_contents-1)
      if len_ball_draw == num : return self.ball_draw
      elif len_contents == 1  :
        self.ball_draw.append( self.contents.pop(0) )
        return self.ball_draw
      else : 
        self.ball_draw.append( self.contents.pop(rand_ball) )
        len_contents -= 1
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  match_draw = 0
  check = []
  print(f'Contents : {hat.items}\n')

  for n in range(num_experiments) :
    print('-----------------')
    print(f'Draw no.{n} :')
    print('-----------------')
    draw_balls = hat.draw(num_balls_drawn)
    count_draw = {}
    for db in draw_balls : count_draw[db] = draw_balls.count(db)
    # print(f'check {n} :\n')
    print(f'draw balls     : {draw_balls}')
    print(f'count draw     : {count_draw}')
    print(f'expected balls : {expected_balls}')
  
    for key, val in expected_balls.items() :
      if key in count_draw.keys() :
        c = expected_balls[key] == count_draw[key]
      # print(f'{c}\n')
    
  # return probability

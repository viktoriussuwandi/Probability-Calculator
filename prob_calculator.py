import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs) :
    self.contents = [ key for key,val in kwargs.items() for i in range(val) ]
    
  def draw(self, num = 0) :
    min_val = min(num, len(self.contents))
    pick_balls = [ self.contents.pop( random.randrange(len(self.contents)) ) 
                   for i in range(min_val) 
                 ]
    return pick_balls
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments) :
  match_drawn = 0
  for i in range(num_experiments) :
    
    # create copy of class
    class_hat = copy.deepcopy(hat)
    
    # count each drawn
    pick_balls       = class_hat.draw(num_balls_drawn)
    pick_balls_count = {}
    for pb in pick_balls : pick_balls_count[pb] = pick_balls.count(pb)
    
    # compare drawn balls with expected balls
    comparisson    = [ (True if (key in pick_balls_count.keys() and pick_balls_count[key] >= val) else False)
                         for (key, val) in expected_balls.items() ]
    compare_result = comparisson.count(True) == len(expected_balls.keys())
    match_drawn   += 1 if compare_result == True else 0
    
  # count probability of all expected and match drawn
  probability = round((match_drawn/num_experiments),3)
  
  return probability

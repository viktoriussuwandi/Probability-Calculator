# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

# prob_calculator.random.seed(95)
# hat = prob_calculator.Hat(blue=4, red=2, green=6)
# print(hat.draw(3))

# probability = prob_calculator.experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=10)
# print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)

def test() :
  import random
  arr1 = [ 
    'a','b','c','d','e',
    'a','b','c','d','e',
    'b','c','d','e',
    'c','d','e',
    'd','e',
    'e'
  ]
  arr2 = {}
  for i in arr1 : arr2[i] = arr1.count(i)
  print(arr2)
# test()

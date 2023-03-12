# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

# --------------------TEST 1----------------------------------
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=10
)
print("Probability Test 1 : ", probability)

# --------------------TEST 2----------------------------------
hat = prob_calculator.Hat(blue=3,red=2,green=6)
probability = prob_calculator.experiment(
  hat=hat, 
  expected_balls={"blue":2,"green":1}, 
  num_balls_drawn=4, 
  num_experiments=1000
)
print("Probability Test 2 :", probability)

# --------------------TEST 3----------------------------------
hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = prob_calculator.experiment(
  hat=hat, 
  expected_balls={"yellow":2,"blue":3,"test":1}, 
  num_balls_drawn=20, 
  num_experiments=10000
)
print("Probability Test 3 :", probability)

# --------------------------------------------------------------------------------------------
# Run unit tests automatically
main(module='test_module', exit=False)

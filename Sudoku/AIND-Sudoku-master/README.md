# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver
# Author:  Ramin Mohammadi

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
First need to iterate through all possible units and pick first unit which have value length equal to 2 as main twin,
then find other boxs which they have value equal to main twin which their id is not the same and save them as possible twin.
Then i have search through all possible unit and found units which they have digits from main twin
and they are not a possible twin, then replace main twin digits from their value.

Constraint propagation here was so clear, as we are looking for twins and then limit over search to their pairs, then for all pairs which have
constriant ( lenght of their value greater than 2) we remove the digits.
also by using recursive functions ( search and reduce_puzzle) we have solved the Sudoku.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?
Same as old constraints, here we just have new units added to all units which says among the two main diagonals, the numbers 1 to 9 should all appear exactly once.



### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - Fill in the required functions in this file to complete the project.
* `test_solution.py` - You can test your solution by running `python -m unittest`.
* `PySudoku.py` - This is code for visualizing your solution.
* `visualize.py` - This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.


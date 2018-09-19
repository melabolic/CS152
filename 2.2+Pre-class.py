

# **You are required to solve the following search problem in Python using a breadth-first approach, by adding in code at the places marked "insert code here"
# Each state is represented by an integer**
# 
# For a state k, the two successor states are 2k and 2k+1 (in this order)
# 
# Starting at initial state 1, the goal is to reach state 1024.
# 
# This code makes use of the class deque in the collections package. You may need to look up the appropriate member functions to add and remove frontier elements.


# Initial state
state = 1

# Define the goal here
goal = 1024

# Frontier; deque functions like the queue
from collections import deque
frontier = deque([state])

# Step counter (should take 10 steps)
steps = 0

# Breadth-first search algorithm (continue while there are nodes in the frontier)
while frontier:
    # [INSERT CODE HERE] Implement a breadth-first search to reach the goal state from the initial state.
    # The search should terminate once the goal is reached.
    # Remember to increment the step counter to keep track of how many steps the search takes!
    # You will need to modify the placeholder code below.
    k = frontier.popleft() # taking out the first term and generating its children
    frontier.append(2*k)
    steps += 1
    if frontier[0] == goal:
        break
    
    frontier.append(2*k+1)
    steps += 1
    #print frontier, steps
    if frontier[1] == goal:
        break
    
# Find the length of the frontier by changing the line below.
frontier_size = len(frontier)
    

print("Breadth-first search terminated after %d steps\n" % steps)
print("Size of frontier at termination is %d" % frontier_size)


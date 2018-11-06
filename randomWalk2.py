# What is the longest random walk you can take so that on average you end up
# 4 blocks or fewer from home?
# If more than 4 blocks pay for a transport home
import random

def random_walk_2(n):
    """ Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        
        x += dx
        y += dy
    return (x, y)

#for i in range(25):
#   walk = random_walk_2(10)
#    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))
    
#=============================================================================
#           MONTE CARLO METHOD 
# Conduct thousands of random trials and compute the pacentage of random walks
# that end in a short walk home
#=============================================================================

number_of_walks = 20000

for walk_length in range(1, 50):
    no_transport = 0 # number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        
        if distance <= 4:
            no_transport += 1
            
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length, "/ % no of transport = ", 
          100*no_transport_percentage)
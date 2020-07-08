import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_belief=[[] for i in range(len(grid))]
    normalizer = 0

    #
    # TODO - implement this in part 2
    #
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col]==color):
                new_prob = beliefs[row][col]*p_hit
                new_belief[row].append(new_prob)
            
            else:
                new_prob = beliefs[row][col]*p_miss
                new_belief[row].append(new_prob)
            
            normalizer += new_prob
        
    for row in range(len(new_belief)):
        for col in range(len(new_belief[0])):
            new_belief[row][col] = new_belief[row][col]/normalizer
    return new_belief

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
#             pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
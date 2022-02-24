
# Wumpus World Class
# Humberto Barrantes
# 2022

# Imports

import numpy as np
from random import randint

class WumpusWorld:
    
    def __init__(self, default=True):
        if default:
            self.world = np.matrix([    
                ['S',       '',         'B',        'P'], 
                ['W',       'B,S,G',    'P',        'B'], 
                ['S',       '',         'B',        ''], 
                ['',        'B',        'P',        'B']
            ])
        else:
            self.world = self.create_world()
    
    def create_world(self):
        temp_world = np.zeros((4,4), dtype=str)

        components = []
        while len(components) < 3:
            row = randint(0,3)
            col = randint(0,3)
            if row != 0 and col != 0 and temp_world[row][col] == '':
                temp_world[row][col] = 'P'
                components.append(['P', [row, col]])
                
        while len(components) < 4:
            row = randint(0,3)
            col = randint(0,3)
            if row != 0 and col != 0 and temp_world[row][col] == '':
                temp_world[row][col] = 'W'
                components.append(['W', [row, col]])
                
        while len(components) < 5:
            row = randint(0,3)
            col = randint(0,3)
            if row != 0 and col != 0 and temp_world[row][col] == '':
                temp_world[row][col] = 'G'
                components.append(['G', [row, col]])

        for t, pos in components:
            if pos[0] + 1 < 4:
                self.create_stench_and_breeze(temp_world, pos[0]+1, pos[1], t == 'W')
            if pos[0] - 1 > 0:
                self.create_stench_and_breeze(temp_world, pos[0]-1, pos[1], t == 'W')
            if pos[0] + 1 < 4:
                self.create_stench_and_breeze(temp_world, pos[0], pos[1]+1, t == 'W')
            if pos[1] - 1 > 0:
                self.create_stench_and_breeze(temp_world, pos[0], pos[1]-1, t == 'W')
        
        return temp_world


    def create_stench_and_breeze(self, temp_world, row, col, stench):
        if stench:
            if temp_world[row][col] == '':
                temp_world[row][col] = 'S'
            else:
                temp_world[row][col] += ',S'
        else:
            if temp_world[row][col] == '':
                temp_world[row][col] = 'B'
            else:
                temp_world[row][col] += ',B'
            

    def get_pos(self, wld, col, row):
        return wld[4-row, col-1]


    def cell(self, col, row):
        return self.get_pos(self.world, col, row).split(",")


    def view(self):
        return self.world
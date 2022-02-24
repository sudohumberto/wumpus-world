
# Wumpus World Solution
# Humberto Barrantes
# 2022


# Imports

import numpy as np
import pandas as pd

from WumpusWorld import *
from Agent import *

# Main

#world = WumpusWorld() 
#agent = Agent(world, 1, 1)

#print("Agent is on", agent.loc())
#print("Agent Perceives", agent.perceives())

wumpus_world = WumpusWorld()
agent = Agent(wumpus_world, 1, 1)

print(wumpus_world.world)

agent.find_gold()

import topogenesis as tg
import numpy as np

# Environment class
class environment():
    def __init__(self):
        pass

    def lattice_update(self):
        pass

    def agents_action(self):
        pass

    def agent_evaluation(self):
        pass
    
    def initialization(self):
        pass
    
    def lattice_check(self):
        pass
    
    def agent_check(self):
        pass

# Agent class
class agent():
    def __init__(self):
        pass

    def evaluation(self):
        pass

    def action(self):
        pass

    # add spatial behaviors as methods


# Dynamic Lattice class
class dynamic_lattice(tg.lattice):
    def __init__(self):
        pass

    def euclidian_distance(self):
        pass

    def manifold_distance(self):
        pass

    def sightline(self):
        pass

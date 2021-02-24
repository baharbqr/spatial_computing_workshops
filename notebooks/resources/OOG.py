import topogenesis as tg
import numpy as np
import pandas as pd

# Environment class
class environment():
    def __init__(self, avail_lattice : tg.lattice ,lattices : dict, agents : dict):
        self.agents = agents
        self.lattices = lattices

        #TODO: construct occupation lattice
        #TODO: extract lattice bounds
        #TODO: extract lattice shape
        #TODO: run initialization

        #TODO: do we need distance matrix?
        
        pass

    def all_lattice_update(self):
        # TODO: run lattice update on all dynamic lattices
        pass

    def lattice_update(self, lattice_key: str):
        # TODO: recompute the specified lattice
        pass

    def all_agents_action(self):
        # TODO: run the action method of all agents
        pass

    def agents_action(self, agent_key: str):
        # TODO: run the action method of specified agents
        pass

    def all_agent_evaluation(self):
        # TODO: run the evaluation method of all agents
        pass

    def agent_evaluation(self, agent_key: str):
        # TODO: run the evaluation method of specified agents
        pass
    
    def initialization(self):
        # TODO: run the lattice check
        # TODO: run the agent check
        # TODO: check if the preferences of agents matches with the provided lattices
        pass
    
    def lattice_check(self):
        # TODO: check if all latices have the same shape
        # TODO: check if all latices have the same bounds
        # TODO: check if all latices have valid values
        pass
    
    def agent_check(self):
        pass

# Agent class
class agent():
    def __init__(self, key: str, preferences: dict, stencils: list, origin: list = None, behaviors: dict = None):
        # TODO: Set all the preferences as attributes
        # TODO: Set all the behaviors and their parameter as attributes
        # TODO: Run find_seed if the origin is not provided
        # TODO: initialize the agent's occupation lattice
        # TODO: initialize the agent's available neighbour lattice per stencil
        # TODO: add agent satisfaction
        pass

    def find_seed(self):
        # TODO: run the initial seed finding
        pass

    def evaluation(self):
        # TODO: evaluate the agents satisfaction based on the value of it's voxels
        pass

    def action(self):
        # TODO: run all the specified behaviors of the agents with their corresponding parameters
        pass


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

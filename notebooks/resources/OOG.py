from numpy.lib.function_base import select
import topogenesis as tg
import numpy as np
import pandas as pd

# Environment class
class environment():
    def __init__(self, avail_lattice : tg.lattice ,lattices : dict, agents_dict : dict, stencils: list):
        self.lattices = lattices
        self.lattice_names = [lattices.keys()]
        self.avail_lattice = avail_lattice
        #TODO: construct occupation lattice
        self.occ_lattice = avail_lattice * 0 - 1
        #TODO: extract lattice bounds
        self.bounds = avail_lattice.bounds
        #TODO: extract lattice shape
        self.shape = avail_lattice.shape
        #TODO: run initialization
        self.initialization(agents_dict)

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

    def agent_action(self, agent_key: str):
        # TODO: run the action method of specified agents
        pass

    def all_agents_evaluation(self):
        # TODO: run the evaluation method of all agents
        pass

    def agent_evaluation(self, agent_key: str):
        # TODO: run the evaluation method of specified agents
        pass
    
    def all_agents_initialization(self, agents_dict):
        # TODO: run the initialization  of all agents
        env_agents = {}
        for name, a in agents_dict.items():
            # TODO: Check if the agents preferences are matching with the environment lattices
            agent_preferences = a["preferences"].keys()
            # TODO: Check if the specified stencils by agent is available in the environment stencils
            # TODO: Run agent initialization method
            env_agents[name] = agent(name, self, a["preferences"], a["stencil_names"], a["origin"], a["behaviors"])
        
        self.agents = env_agents

    def initialization(self, agents_dict):
        avail_flat = self.avail_lattice.flatten()
        avail_index = np.array(np.where(self.avail_lattice == 1)).T
        # cur_occ_lattice = tg.to_lattice(np.copy(self.occ_lattice), self.occ_lattice)
        # TODO: run the lattice check
        self.lattice_check()
        # TODO: check if the preferences of agents matches with the provided lattices
        self.all_agents_initialization(agents_dict)
        pass
    
    def lattice_check(self):
        shapes, bounds, mins, maxs = [],[],[],[]
        # iterate over all lattices
        for name, l in self.lattices.items():
            shapes.append(l.shape)
            bounds.append(l.bounds.flatten())
            mins.append(l.min)
            maxs.append(l.max)
        # access lattice names in self.lattice_names

        # TODO: check if all latices have the same shape
        shape_check = np.all(np.array(shapes) == self.shape)
        # TODO: check if all latices have the same bounds
        bound_check = np.all(np.array(bounds) == self.bounds.flatten())
        # TODO: check if all latices have valid values
        mins_check = np.array(mins).astype(float).min() >= 0.0
        mins_check = np.array(maxs).astype(float).max() <= 1.0

        # TODO: Check if there is any invalid entry in the lattices (infinity, NaN)

        pass

# Agent class
class agent():
    def __init__(self, name: str, env: environment, preferences: dict, stencil_names: list, origin: list = None, behaviors: dict = None):
        self.name = name
        self.stencils = env.stencils[stencil_names]

        # TODO: Set all the preferences as attributes
        self.preferences = preferences

        # TODO: Set all the behaviors and their parameter as attributes
        self.behaviors = behaviors

        # TODO: Run find_seed if the origin is not provided
        if origin:
            self.origin = origin
        else:
            self.origin = agent.find_seed(self, env)

        # TODO: initialize the agent's occupation lattice
        occ_lat = env.occ_lattice
        # TODO: initialize the agent's available neighbour lattice per stencil
        
        # TODO: add agent satisfaction
        self.satisfaction = 0.0
        
        pass


    def find_seed(self, env: environment):
        # TODO: run the initial seed finding
        agn_num = len(self.preferences)
        select_id = np.random.choice(len(env.avail_index), agn_num)
        return env.avail_index[select_id]
    
    def update_occ_lattice(self, env:environment):
        for agn in self.origin:
            env.occ_lattice
        pass

    def evaluation(self, env : environment):
        # TODO: evaluate the agents satisfaction based on the value of it's voxels

        pass

    def action(self):
        # TODO: run all the specified behaviors of the agents with their corresponding parameters
        pass

#class particle():
    #def __init__(self, stencil_names : list, base, agent_name : str):
        #pass
    #def find_neigh(self):
        #pass
    


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

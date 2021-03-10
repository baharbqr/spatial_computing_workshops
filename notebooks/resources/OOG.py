from numpy.lib.function_base import select
import topogenesis as tg
import numpy as np
import pandas as pd
from topogenesis.datastructures.datastructures import lattice

# Environment class
class environment():
    def __init__(self, avail_lattice : tg.lattice ,lattices : dict, agents_dict : dict, stencils: dict):
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

        self.stencils = stencils
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
            agn_id = agents_dict.keys().index(name)
            # TODO: Check if the specified stencils by agent is available in the environment stencils
            # TODO: Run agent initialization method
            env_agents[name] = agent(agn_id, name, self, a["preferences"], a["stencil_names"], a["origin"], a["behaviors"])
        
        self.agents = env_agents

    def initialization(self, agents_dict):
        avail_flat = self.avail_lattice.flatten()
        avail_index = np.array(np.where(self.avail_lattice == 1)).T
        # cur_occ_lattice = tg.to_lattice(np.copy(self.occ_lattice), self.occ_lattice)
        # TODO: run the lattice check
        self.lattice_check()
        # TODO: check if the preferences of agents matches with the provided lattices
        self.all_agents_initialization(agents_dict)
        self.define_neighbour_lattice()
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

    def define_neighbour_lattice(self):
        self.neigh_matrix = {}
        for stencil in self.stencils:
            self.neigh_matrix[stencil] = self.avail_lattice.find_neighbours(self.stencils[stencil], order='dist')

# Agent class
class agent():
    def __init__(self, aid: int, name: str, env: environment, preferences: dict, stencil_names: list, origin: list = None, behaviors: dict = None):
        self.name = name
        self.stencils = env.stencils[stencil_names]
        self.id = aid
        # TODO: Set all the preferences as attributes
        self.preferences = preferences

        # TODO: Set all the behaviors and their parameter as attributes
        self.behaviors = behaviors

        # TODO: Run find_seed if the origin is not provided
        if origin:
            self.origin = origin
        else:
            self.origin = agent.find_seed(self, env)

        # TODO: initialize the agent's occupation lattice ----> This is tha lattice that describes the voxels occupied by this agent only
        self.occ_lattice = env.occ_lattice == aid
        # Bahar: In the line above, what does "== aid" do? Does it turn all the ones to the agent number?
        #        If yes, why should the agent's occ lattice contains the agent id itself? Isn't it better to keep it as 1 and 0's and
        #        wherever needed  multiply it with its id?
        self.update_env_lattices(env)

        # TODO: initialize the agent's available neighbour lattice per stencil
        self.neighbours = {}
        self.update_neighbor(env)
                
        # TODO: add agent satisfaction
        self.satisfaction = {}
        self.satisfaction = self.evaluation(env)


    def find_seed(self, env: environment):
        # TODO: run the initial seed finding
        agn_num = len(self.preferences)
        select_id = np.random.choice(len(env.avail_index), agn_num)
        return env.avail_index[select_id]
    
    def update_env_lattices(self, env:environment):
        env.occ_lattice[self.occ_lattice] = self.id
        env.avail_lattice[self.occ_lattice] = 0

    def evaluation(self, env : environment):
        # TODO: evaluate all the voxels based on the agents preferences
        # Bahar: We should return value here, right?
        eval_lat = tg.to_lattice(np.ones(self.occ_lattice.shape), self.occ_lattice)
        self.eval_lat = eval_lat

    @property
    def satisfaction(self):
        # TODO: compute the agents satisfaction based on the value of it's voxels
        return np.mean(self.eval_lat[self.occ_lattice])

    @property
    def bounding_box(self):
        b_box = np.copy(self.occ_lattice)
        b_slice = np.nonzero(self.occ_lattice)
        b_box[b_slice.min(1,2): b_slice.max(1,2) + 1, b_slice.min(0,2): b_slice.max(0,2) + 1, b_slice.min(0,1) : b_slice.max(0,1) + 1] = 1
        return b_box
    
    @property
    def shape(self):
        return np.nonzero(self.bounding_box).shape

    # Bahar: I wasn't sure if in python we can have a function with two different sets of arguments. I did a quick search but didn't find anything.
    #        Also I wasn't sure how we will end up with the data type we're passing to the function. Personally, I'm fond of lattices.
    #        Also I THINK it might be a good idea to declare behaviors as @property like satisfaction, but I don't know how it might work. So
    #           for now they are methods in a dictionary... I guess.
    def beh_occupy(self, vox_id, env : environment):
        for id in vox_id:
            self.occ_lattice[np.unravel_index(id, self.occ_lattice.shape)] = 1.0
            self.update_env_lattices(env)

    def beh_occupy(self, vox_lattice : tg.lattice, env : environment):
        self.occ_lattice[vox_lattice] = 1.0
        self.update_env_lattices(env)
    
    def beh_leave(self, vox_id, env : environment):
        for id in vox_id:
            self.occ_lattice[np.unravel_index(id, self.occ_lattice.shape)] = 0.0
            self.update_env_lattices(env)

    def beh_leave(self, vox_lattice : tg.lattice, env : environment):
        self.occ_lattice[vox_lattice] = 0.0
        self.update_env_lattices(env)

    # Bahar: check this one please :)
    #        Although it was fun playing with the data in my head, I think there might be a simpler way.
    def beh_find_neighbour (self, stencils : list, env: environment):
        neighbourhood = {}
        for stencil in stencils:
            all_neighbours = env.neigh_matrix[np.where(np.array(self.occ_lattice).flatten() == 1.0)].reshape(tuple([-1] + list(self.occ_lattice.shape))).sum(0)
            neighbourhood[stencil]  = all_neighbours[np.where(all_neighbours == 1.0)]
        return neighbourhood

    # TODO : box character
    def char_embed_box(self):
        self.bounding_box *= self.character[box]
    
    # TODO : depth behavior
    def char_building_depth(self, env : environment):
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

import random

from mesa import Agent

from wolf_sheep.random_walk import RandomWalker


class Sheep(RandomWalker):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the RandomWalker.
    '''

    energy = None

    def __init__(self, pos, model, moore, energy=None):
        super().__init__(pos, model, moore=moore)
        self.energy = 10

    def step(self):
        '''
        A model step. Move, then eat grass and reproduce.
        '''

        if self.model.grass:
            # If there is grass available, eat it
            this_cell = self.model.grid.get_cell_list_contents([self.pos])
            grass_patch = [obj for obj in this_cell
                           if isinstance(obj, GrassPatch)][0]
  
#            # find if any other sheep is in this cell
#            others = [obj for obj in this_cell if isinstance(obj, GrassPatch)]
#            if len(others)>1:
#                for other in others:
#                    self.energy += other.energy
#                    other.energy = 0
  

            # try for splitting into two
            if grass_patch.number<=0:
                self.random_move()
                self.energy -= 2
            else:
                grass_patch.number -= self.energy
                self.energy +=1
    
        # Death
        if self.energy <= 0:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            


class GrassPatch(Agent):
    '''
    A patch of grass that grows at a fixed rate and it is eaten by sheep
    '''

    def __init__(self, pos, model, fully_grown , countdown):
        '''
        Creates a new patch of grass

        Args:
            grown: (boolean) Whether the patch of grass is fully grown or not
            countdown: Time for the patch of grass to be fully grown again
        '''
        super().__init__(pos, model)
        self.pos = pos
        self.fully_grown = fully_grown
        self.countdown = countdown
        if pos[0]>= 0 and pos[0] <3:
            self.number = 2
        else:
            self.number = 1

    def step(self):
        if self.number < 100:
            self.number    += 1
        self.countdown -= 1
        if self.number <= 0:
            self.fully_grown = False
            self.countdown   = self.model.grass_regrowth_time
        else:
            self.fully_grown = True
        

import random

from mesa import Agent

from wolf_sheep.random_walk import RandomWalker


class Sheep(RandomWalker):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the RandomWalker.
    # Energy is the number of refugees.
    '''

    energy = None

    def __init__(self, pos, model, moore, energy=None):
        super().__init__(pos, model, moore=moore)
        # initialize always 1 refugee household
        self.energy = 10

    def step(self):
        '''
        A model step. Move, then eat grass and reproduce.
        '''
        self.random_move()

        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        grass_patch = [obj for obj in this_cell if isinstance(obj, GrassPatch)][0]
        
        # If there is grass available, eat it
        if grass_patch.fully_grown:
            grass_patch.number -= self.energy
            # if resources finished, divide in number and let half of the people go
            if grass_patch.number < 1:
                grass_patch.fully_grown = False

        else:
            if self.model.grass:
                self.energy /= 2
            lamb = Sheep(self.pos, self.model, self.moore, self.energy)
            self.model.grid.place_agent(lamb, self.pos)
            self.model.schedule.add(lamb)
                  
                  
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
        self.fully_grown = fully_grown
        self.countdown = countdown
        self.number = 2

    def step(self):
        if not self.fully_grown:
            if self.countdown <= 0:
                # Set as fully grown
                self.fully_grown = True
                self.number += 1
                self.countdown = self.model.grass_regrowth_time
            else:
                self.countdown -= 1
        else:
            self.countdown <=0
            self.number += 1
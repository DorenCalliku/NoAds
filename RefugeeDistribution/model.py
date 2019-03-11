'''
'''

import random

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from wolf_sheep.agents import Sheep, GrassPatch
from wolf_sheep.schedule import RandomActivationByBreed


class WolfSheepPredation(Model):

    verbose = False  # Print-monitoring

    def __init__(self, height=10, width=10,
                 initial_sheep=10, 
                 grass=False, grass_regrowth_time=30, sheep_gain_from_food=4):

        # Set parameters
        self.wave = 5
        self.height = height
        self.width  = width
        self.initial_sheep   = initial_sheep
        self.grass = grass
        self.grass_regrowth_time = grass_regrowth_time
        self.sheep_gain_from_food = sheep_gain_from_food

        self.schedule = RandomActivationByBreed(self)
        self.grid = MultiGrid(self.height, self.width, torus=False)
        self.datacollector = DataCollector(
            {"Sheep": lambda m: m.schedule.get_breed_count(Sheep)})

        # Create grass patches
        if self.grass:
            for agent, x, y in self.grid.coord_iter():

                # only because of the start
                fully_grown = random.choice([True])

                if fully_grown:
                    countdown = self.grass_regrowth_time
                else:
                    countdown = random.randrange(self.grass_regrowth_time)

                patch = GrassPatch((x, y), self, fully_grown, countdown)
                self.grid.place_agent(patch, (x, y))
                self.schedule.add(patch)

        self.running = True

    def step(self):
        # find if the last two columns are full of grass, if so, add sheeps
        if self.wave < 0:
            enter = True
            for i in (0,self.height-1):
                this_cell = self.grid.get_cell_list_contents((self.width - 1,i))
                grass_patch = [obj for obj in this_cell if isinstance(obj, GrassPatch)][0]
                if not grass_patch.fully_grown:
                    enter = False
#                this_cell = self.grid.get_cell_list_contents((self.width - 2,i))
#                grass_patch = [obj for obj in this_cell if isinstance(obj, GrassPatch)][0]
#                if not grass_patch.fully_grown:
#                    enter = False
#                    
            # create sheep
            if enter:
                x = self.width - 1
                y = 1 #random.randrange(self.height)
                energy = random.randrange(2 * self.sheep_gain_from_food)
                sheep = Sheep((x, y), self, True, energy)
                self.grid.place_agent(sheep, (x, y))
                self.schedule.add(sheep)
                enter = True
            self.wave = 5
        self.wave -= 1
        
        self.schedule.step()
        self.datacollector.collect(self)
        if self.verbose:
            print([self.schedule.time,self.schedule.get_breed_count(Sheep)])
        

            

    def run_model(self, step_count=20):

        if self.verbose:
            print('Initial number sheep: ',
                  self.schedule.get_breed_count(Sheep))

        for i in range(step_count):
            self.step()

        if self.verbose:
            print('')
            print('Final number sheep: ',
                  self.schedule.get_breed_count(Sheep))

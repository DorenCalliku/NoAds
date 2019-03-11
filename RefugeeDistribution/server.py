from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule

from wolf_sheep.agents import Sheep, GrassPatch
from wolf_sheep.model import WolfSheepPredation


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {"Shape": "circle",
                 "Filled": "true"}

    if type(agent) is Sheep:
        if agent.energy > 10:
            portrayal["Color"] = "#2F4F4F"
        elif agent.energy > 0:
           portrayal["Color"] = "#A9A9A9"
        else:
            portrayal["Color"] = "#000000"
        
        portrayal["r"] = 0.8
        portrayal["Layer"] = 1       
        portrayal["text"] = round(agent.energy, 1)
        portrayal["text_color"] = "Black"        
        
    elif type(agent) is GrassPatch:
        if agent.number>10:
            portrayal["Color"] = "#8FBC8F"
        elif agent.number>0:
            portrayal["Color"] = "#98FB98"
        else:
            portrayal["Color"] = "#D6F5D6"
        portrayal["Shape"] = "rect"
        portrayal["Layer"] = 0
        portrayal["text"] = round(agent.number, 1)
        portrayal["text_color"] = "Black"   
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal

canvas_element = CanvasGrid(wolf_sheep_portrayal, 10, 10, 25*4*10,25*4*10)
chart_element  = ChartModule([{"Label": "Sheep", "Color": "#666666"}])

server = ModularServer(WolfSheepPredation, [canvas_element, chart_element],
                       "Refugee Crisis", grass=True)
# server.launch()

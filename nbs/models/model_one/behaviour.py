# behaviour.py
import random

from helipad import Helipad

from .model import *

def add_behaviour(model: Helipad):

    model.hooks.add('modelPreSetup', modelPreSetup)
    model.hooks.add('modelPostSetup', modelPostSetup)
    model.hooks.add('agentInit', agentInit)
    model.hooks.add('patchInit', patchInit)
    model.hooks.add('patchStep', patchStep)
    model.hooks.add('agentStep', agentStep)
    model.hooks.add('modelStep', modelStep)

    model.events.add('stop_after', stop_after)

    return model

def modelPreSetup(model):
    # print("modelPreSetup")
    pass

def modelPostSetup(model):
    # print("modelPostSetup")
    print(f"patches: {len(model.patches)}")
    print(f"agents: {len(model.agents['agent'])}")
    # setup: percent_best_land
    # diffuse maxiumum to neighbouring patches

def agentInit(agent, model):
    # print("agent init")
    # print(f"apos{agent.position}-appost{agent.patch.position}")
    agent.stocks['min_harvest_level'] = random.randint(0, 10)
    pass

def patchInit(patch, model):
    # print("patch init")
    # print(f"ppos{patch.position}")
    # randomly between min and maxmium patch amount
    patch.stocks['apples'] = random.randint(0, 50)

def patchStep(patch, model, stage):
    # print("patch step")
    if stage==2:
        patch.stocks['apples'] += model.param("regrowth_rate") # Regrow
        pass

def agentStep(agent, model, stage):
    # print("agent step")
    if stage==1:
        # find next location and move to it - random
        # move one square
        prospects = agent.patch.neighbors
        agent.orientTo(random.choice(prospects))
        agent.forward()            
        # harvest
        # if patch apples > min_harvest_amount
        harvest = False

        if agent.patch.stocks['apples'] > agent.stocks['min_harvest_level']:
            agent.patch.stocks['apples'] -= 1
            agent.stocks['apples'] += 1
            harvest = True

        if not harvest:
            agent.stocks['min_harvest_level'] -= 1 # lower for next time
        else:
            agent.stocks['min_harvest_level'] += 1 # raise minimum for next time

        # pass

def modelStep(model, stage):
    # print("model step")
	pass

def stop_after(model):
    return model.t >= 400

from agent import Agent
from PDWorld import World
from PDWorld import Node
import random
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
import pygame
from Visualize import Visual

class E2:
    agent = Agent(0,4,False)
    havePackageWorld = World()
    noPackageWorld = World()

    show = Visual()
    # show.run_visual(noPackageWorld, havePackageWorld, agent)
    # show.quit()

    for i in range(200):
        oldAgent = copy.deepcopy(agent)
        if not (agent.havePackage):
           world = noPackageWorld
           world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)
            
        SelectMove.PRANDOM(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, 0.5)
        if(world.isCompleteDelevery()):
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            print("MapReset")
    #Show progress after PRANDOM
    show.run_visual(noPackageWorld, havePackageWorld, agent)

    #Show progress at fixed intervals
    for i in range(7800):
        oldAgent = copy.deepcopy(agent)
        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)
            
        SelectMove.PEPLOIT(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, 0.5)
        if i == 1799:
            show.run_visual(noPackageWorld, havePackageWorld, agent)
        elif i == 3799:
            show.run_visual(noPackageWorld, havePackageWorld, agent)
        elif i == 5799:
            show.run_visual(noPackageWorld, havePackageWorld, agent)
        if(world.isCompleteDelevery()):
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            print("MapReset")
            
    #show = Visual()
    show.run_visual(noPackageWorld, havePackageWorld, agent)
    show.quit()

    #update score after every move
    #SelectMove.PEXPLOIT(agent, world, printMove= False)
    #SelectMove.PRANDOM(agent, world, printMove= False)
    #SelectMove.PGREEDY(agent, world, printMove= False)
    # print("Agent is at x: ", agent.x, " y: ", agent.y)

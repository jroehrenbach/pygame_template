# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:31:46 2019

@author: jakob
"""


from game import Game
import observer as obs
from cube import Cube

game = Game((800, 600), "cube", use_opengl=True)

game._obs.commands = {
        1: obs.LMB(game,True), # left mouse button
        "p": obs.p_key(game)
}

try:
    game.run(Cube)
except:
    game._terminate(True)
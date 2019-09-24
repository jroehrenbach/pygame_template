# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:31:46 2019

@author: jakob
"""


from game import Game
import observer as obs


game = Game(400, 400, "test")

game._obs.commands = {
        1: obs.LMB(game), # left mouse button
        "p": obs.p_key(game)
}

game.run()

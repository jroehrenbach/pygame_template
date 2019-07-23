# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:27:49 2019

@author: jakob
"""



import pygame
from time import time
from barrier import Rect, Ground



# =============================================================================
# class Command:
#     
#     def __init__(self, game, keyname):
#         self.game = game
#         self.keyname = keyname
#     
#     def poll(self, keylist):
#         
#     
#     def execute(self):
#         return
# 
# class Cmd_move_up(Command):
#     
#     def execute(self):
#         self.game.screen.
# =============================================================================


class Game:
    
    def __init__(self, w, h):
        pygame.init()
        self.surf = pygame.display.set_mode((w, h))
        pygame.display.set_caption("car_game")
        self.screen = Rect(np.zeros(2), np.array([w,h])/2)
        self.screen_angle = 0
        
        self.commands = {""}
        
        self.time = time()
        self.ms_per_frame = 30
        self.rgb_background = (0,0,160)
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        #keys = pygame.key.get_pressed()
    
    def _draw(self):
        self.surf.fill(self.rgb_background)
        if hasattr(self, "ground"):
            self.ground.draw(self.surf, self.screen, self.screen_angle)
            self.screen_angle += 0.1
            #self.screen.center[0] += 1
        pygame.display.update()
    
    def _balance(self, PRINT_SHIFT=False):
        shift = round((time() - self.time) * 1000)
        if PRINT_SHIFT: print(shift)
        if shift<self.ms_per_frame:
            pygame.time.delay(self.ms_per_frame - shift)
        self.time = time()
    
    def run(self):
        self.running = True
        while self.running:
            self._handle_events()
            self._draw()
            self._balance()
        pygame.quit()


import numpy as np
game = Game(400,400)
game.screen.center = np.array([200,200])
game.ground = Ground((1000,1000))
game.ground.set_barrier([[100,100],[300,300]])
game.ground.set_barrier([[250,150],[150,250]])
game.run()
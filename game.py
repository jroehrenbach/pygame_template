# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:27:49 2019

@author: jakob
"""



import pygame
from time import time



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
    
    def __init__(self, w, h, name=""):
        pygame.init()
        self.surf = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        
        self.commands = {""}
        
        self.time = time()
        self.ms_per_frame = 30
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        #keys = pygame.key.get_pressed()
    
    def _draw(self):
        self.surf.fill((0,0,0))
        pygame.display.update()
    
    def _balance(self, PRINT_SHIFT=False):
        shift = round((time() - self.time) * 1000)
        if PRINT_SHIFT: print(shift)
        if shift<self.ms_per_frame:
            pygame.time.delay(int(self.ms_per_frame - shift))
        self.time = time()
    
    def run(self):
        self.running = True
        while self.running:
            self._handle_events()
            self._draw()
            self._balance()
        pygame.quit()


game = Game(400,400)
game.run()
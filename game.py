# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:27:49 2019

@author: jakob
"""



import pygame
import numpy as np
from time import time


# also pass game for external control
# keydict
# mousedict

class Command:
    
    def __init__(self, game=None):
        self.game = game
    
    def execute(self):
        print("nothing to execute!")

class LMB(Command):
    
    def __init__(self, game):
        Command.__init__(game)
    
    def execute(self):
        pos = pygame.mouse.get_pos()
        print("left mouse button pressed at", pos)



class Game:
    
    def __init__(self, w, h, name=""):
        pygame.init()
        self.surf = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        
        nkeys = 323
        nbuttons = 3
        self.keys = np.array([Command()]*nkeys)
        self.mouse = np.array([Command()]*nbuttons)
        self.pressed_keys = np.zeros(nkeys, bool)
        self.pressed_buttons = np.zeros(nbuttons, bool)
        
        self.mouse[0] = LMB(self)
        
        self.time = time()
        self.ms_per_frame = 30
        
        pygame.mouse.set_pos((w/2,h/2))
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        k = np.array(pygame.key.get_pressed(), bool)
        b = np.array(pygame.mouse.get_pressed(), bool)
        [key.execute() for key in self.keys[k & ~self.pressed_keys]]
        [b.execute() for b in self.mouse[b & ~self.pressed_buttons]]
        self.pressed_keys, self.pressed_buttons = k, b
    
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
            try:
                self._handle_events()
            except:
                self.running = False
            self._draw()
            self._balance()
        pygame.quit()


# =============================================================================
# game = Game(400,400)
# game.run()
# =============================================================================

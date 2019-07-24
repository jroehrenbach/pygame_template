# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:27:49 2019

@author: jakob
"""



import pygame
from time import time


class Command:
    
    def __init__(self, game=None):
        self.game = game
    
    def execute(self, *args):
        print("nothing to execute!")

# example commands
class LMB(Command):
    
    def __init__(self, game):
        Command.__init__(self, game)
    
    def execute(self, position):
        print("left mouse button was pressed at", position)

class p_key(Command):
    
    def __init__(self, game):
        Command.__init__(self, game)
    
    def execute(self):
        if self.game.waiting:
            print("game was unpaused...")
        else:
            print("game was paused...")
        self.game.waiting = ~self.game.waiting


class Game:
    
    def __init__(self, w, h, name=""):
        # initialize pygame and window
        pygame.init()
        self.surf = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        
        # commands for pressed keys/buttons
        self.commands = {
                1: LMB(self), # left mouse button
                "p": p_key(self)
        }
        self.waiting = False
        
        self.time = time()
        self.ms_per_frame = 250
        
        pygame.mouse.set_pos((w/2,h/2))
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button not in self.commands:
                    continue
                self.commands[event.button].execute(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.unicode == "":
                    continue
                if event.unicode not in self.commands:
                    continue
                self.commands[event.unicode].execute()
        
    def _draw(self):
        self.surf.fill((0,0,0))
        # draw stuff
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
            if not self.waiting:
                self._draw()
            self._balance()
        pygame.quit()


# =============================================================================
# try:
#     game = Game(400,400)
#     game.run()
# except:
#     pygame.quit()
#     print("terminated...")
# =============================================================================

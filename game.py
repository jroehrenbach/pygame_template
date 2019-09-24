# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:27:49 2019

@author: jakob
"""


import numpy as np
import pygame
from time import time
from observer import Observer



class Game:
    """pygame wrapper class"""
    
    def __init__(self, shape, name=""):
        """
        Parameters
        ----------
        shape : tuple of ints
            Width and height of screen
        name : str (optional)
            name of game (will be shown above window)
        """
        
        self._obs = Observer(self)
        
        self.waiting = False
        
        self.name = name
        self.shape = np.array(shape)
        self.time = time()
        self.ms_per_frame = 250
        
        
    def _open(self, set_mouse=False):
        # initialize pygame and window
        pygame.init()
        self.surf = pygame.display.set_mode(self.shape)
        pygame.display.set_caption(self.name)
        
        if set_mouse:
            pygame.mouse.set_pos(self.shape / 2)
    
    
    
    def _draw(self):
        """
        Draws everything
        """
        self.surf.fill((0,0,0))
        # draw stuff
        pygame.display.update()
    
    
    
    def _balance(self, PRINT_SHIFT=False):
        """
        Balances game between frames to make it run more smoothly
        
        Parameters
        ----------
        PRINT_SHIFT : bool
            prints time delay to console
        """
        shift = round((time() - self.time) * 1000)
        if PRINT_SHIFT: print(shift)
        if shift<self.ms_per_frame:
            pygame.time.delay(int(self.ms_per_frame - shift))
        self.time = time()
    
    
    def _terminate(self, exception=None):
        """
        Closes pygame and stops game from running
        
        Parameters
        ----------
        exception : AttributeError (optional)
            prints args if passed
        """
        if exception != None:
            print("EXEPTION: ",*exception.args)
        pygame.quit()
        self.running = False
        print("pygame was terminated...")
    
    
    def run(self):
        """
        Loops all game processes while running
        """
        self._open(True)
        self.running = True
        while self.running:
            try:
                self._obs.handle_events()
                if not self.waiting:
                    self._draw()
                self._balance()
            except Exception as e:
                self._terminate(e)
        pygame.quit()


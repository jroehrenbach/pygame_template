# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:16:05 2019

@author: jakob
"""


import pygame
import numpy as np


class Observer:
    
    def __init__(self, game):
        """
        Parameters
        ----------
        game : Game
            Game object the observer will be linked to
        """
        self._game = game
        self.commands = {}
        self.active_keys = []
    
    
    def handle_events(self):
        """
        Goes through events and executes referred commands
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._game.running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button not in self.commands:
                    continue
                self.active_keys.append(event.button)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button not in self.commands:
                    continue
                if event.button in self.active_keys:
                    self.active_keys.remove(event.button)
            
            elif event.type == pygame.KEYDOWN:
                if event.unicode == "":
                    continue
                if event.unicode not in self.commands:
                    continue
                self.active_keys.append(event.unicode)
            
            elif event.type == pygame.KEYUP:
                if event.unicode == "":
                    continue
                if event.unicode not in self.commands:
                    continue
                if event.unicode in self.active_keys:
                    self.active_keys.remove(event.unicode)
        
        for key in self.active_keys:
            self.commands[key].execute()



class Command:
    """base class for all commands (using events)"""
    
    def __init__(self, game=None, lock=False):
        """
        Parameters
        ----------
        game : Game
            Game object the command should be linked to
        lock : bool
            if True command will be executed meanwhile pressed
        """
        self.game = game
        self.lock = lock
        self.activated = False
    
    def execute(self, *args):
        """
        Will have a certain task for derived classes
        
        Parameters
        ----------
        args : args (optional)
            Arguments can be passed in derived classes
        """
        if not self.lock:
            self.activated = False


# example commands
class LMB(Command):
    """linked to left mouse button"""
    
    def __init__(self, game, lock=False):
        Command.__init__(self, game, lock)
    
    def execute(self):
        """
        Parameters
        ----------
        position : tuple
            position of cursor
        """
        #print("left mouse button was pressed at", position)
        right, up = pygame.mouse.get_rel()
        self.game.camera.move(right, up)
        Command.execute(self)



class p_key(Command):
    """linked to <p>"""
    
    def __init__(self, game, lock=False):
        Command.__init__(self, game, lock)
    
    def execute(self):
        """
        Linked game will be paused
        """
        if self.game.waiting:
            print("game was unpaused...")
        else:
            print("game was paused...")
        self.game.waiting = ~self.game.waiting
        Command.execute(self)


# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:16:05 2019

@author: jakob
"""


import pygame




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
                self.commands[event.button].execute(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.unicode == "":
                    continue
                if event.unicode not in self.commands:
                    continue
                self.commands[event.unicode].execute()



class Command:
    """base class for all commands (using events)"""
    
    def __init__(self, game=None):
        """
        Parameters
        ----------
        game : Game
            Game object the command should be linked to
        """
        self.game = game
    
    def execute(self, *args):
        """
        Will have a certain task for derived classes
        
        Parameters
        ----------
        args : args (optional)
            Arguments can be passed in derived classes
        """
        print("nothing to execute!")


# example commands
class LMB(Command):
    """linked to left mouse button"""
    
    def __init__(self, game):
        Command.__init__(self, game)
    
    def execute(self, position):
        """
        Parameters
        ----------
        position : tuple
            position of cursor
        """
        print("left mouse button was pressed at", position)



class p_key(Command):
    """linked to <p>"""
    
    def __init__(self, game):
        Command.__init__(self, game)
    
    def execute(self):
        """
        Linked game will be paused
        """
        if self.game.waiting:
            print("game was unpaused...")
        else:
            print("game was paused...")
        self.game.waiting = ~self.game.waiting

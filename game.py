# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:27:49 2019

@author: jakob
"""


import numpy as np
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL import GL, GLU
from time import time
from observer import Observer

import traceback


class Camera:
    
    def __init__(self, x=0, y=0, z=-5, fov=45, mode="focus_on_center"):
        self.x = x
        self.y = y
        self.z = z
        self.fov = fov
        self.mode = mode
        self.sensitivity = 0.1
        self.right = 0
        self.up = 0
        self.forward = 0
        self.total = 0
    
    def setup(self, shape):
        GLU.gluPerspective(self.fov, shape[0]/shape[1], 0.1, 50.0)
        GL.glTranslatef(self.x, self.y, self.z)
    
    def move(self, right, up, forward=0):
        if self.mode == "focus_on_center":
            self.total = np.sqrt(right**2 + up**2)
            print(right, up, self.total * self.sensitivity)
            self.right, self.up = right, up
    
    def run(self):
            GL.glRotatef(self.total * self.sensitivity,
                         -self.up, -self.right, -self.forward)
        


class Game:
    """pygame wrapper class"""
    
    def __init__(self, shape, name="", use_opengl=False):
        """
        Parameters
        ----------
        shape : tuple of ints
            Width and height of screen
        name : str (optional)
            name of game (will be shown above window)
        """
        
        self.use_opengl = use_opengl
        if use_opengl:
            self.camera = Camera()
        
        self._obs = Observer(self)
        self.waiting = False
        
        self.name = name
        self.shape = np.array(shape)
        self.time = time()
        self.ms_per_frame = 30
        
        
    def _open(self, set_mouse=False):
        # initialize pygame and window
        pygame.init()
        if self.use_opengl:
            pygame.display.set_mode(self.shape, DOUBLEBUF|OPENGL)
            self.camera.setup(self.shape)
        else:
            self.surf = pygame.display.set_mode(self.shape)
        
        pygame.display.set_caption(self.name)
        
        if set_mouse:
            pygame.mouse.set_pos(self.shape / 2)
    
    
    
    def _draw(self, routines=[]):
        """
        Draws everything
        """
        if self.use_opengl:
            GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        else:
            self.surf.fill((0,0,0))
        
        # draw stuff
        if not hasattr(routines, "__getitem__"):
            routines = [routines] if routines!=None else []
        for routine in routines:
            routine()
        
        if self.use_opengl:
            pygame.display.flip()
        else:
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
    
    
    def _terminate(self, print_traceback=False):
        """
        Closes pygame and stops game from running
        
        Parameters
        ----------
        exception : AttributeError (optional)
            prints args if passed
        """
        if print_traceback:
            print(traceback.format_exc())
        pygame.quit()
        self.running = False
        print("pygame was terminated...")
    
    
    def run(self, routines=[]):
        """
        Loops all game processes while running
        """
        self._open(True)
        self.running = True
        while self.running:
            try:
                self._obs.handle_events()
                if not self.waiting:
                    self._draw(routines)
                    self.camera.run()
                self._balance()
            except Exception as e:
                self._terminate(e)
        pygame.quit()

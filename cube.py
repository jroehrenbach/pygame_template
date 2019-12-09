# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:06:51 2019

@author: jroeh
"""

from OpenGL import GL, GLU
import numpy as np

vertices = np.array([
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, 1]
        ])

edges = np.array([
        [0, 1],
        [0, 3],
        [0, 4],
        [2, 1],
        [2, 3],
        [2, 7],
        [6, 3],
        [6, 4],
        [6, 7],
        [5, 1],
        [5, 4],
        [5, 7]
        ])

surfaces = np.array([
        [0, 1, 2, 3],
        [3, 2, 7, 6],
        [6, 7, 5, 4],
        [4, 5, 1, 0],
        [1, 5, 7, 2],
        [4, 0, 3, 6]
        ])

colors = np.array([
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1]
        ])


modelview_matrix = lambda: GL.glGetFloatv(GL.GL_MODELVIEW_MATRIX)


def position(mvm=None):
    if mvm == None:
        mvm = modelview_matrix()
    return mvm.T[3][:3] * mvm[3][3]


def sort_surfaces(mvm=None):
    p = position(mvm)
    dists = np.sqrt(((vertices[surfaces]-p)**2).sum(2)).mean(1)
    surfaces[:] = surfaces[np.argsort(dists)]


def Cube():
    sort_surfaces()
    
    GL.glBegin(GL.GL_QUADS)
    for surface in surfaces:
        for index in surface:
            GL.glColor3fv(colors[index])
            GL.glVertex3fv(vertices[index])
    GL.glEnd()

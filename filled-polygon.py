""" Using OpenGL draw a filled polygon with the following dimensions(8,4;2,4;0,8;3,12;7,12;10,8) hint (GL POLYGON function ) might be useful
a. Write a function to fill the polygon above in Red (#FF0000.)
b. write program to scale up (scaling) the polygon by a factor of 2
c. Write a procedure to fill the interior of a given polygon with shades of asterisks

"""

import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def polygon():
    glBegin(GL_POLYGON)
    #specify coordinates of each vertex
    glVertex2i(8, 4)
    glVertex2i(2, 4)
    glVertex2i(0, 8)
    glVertex2i(3, 12)
    glVertex2i(7, 12)
    glVertex2i(10, 8)
    glEnd()
    glFlush()

def display():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def main():
    glClear(GL_COLOR_BUFFER_BIT) #clear buffer
    glColor3f(1.0, 0.0, 0.0) #set colour to red
    glScalef(2.0, 2.0, 1.0) #scale up by a factor of 2
    polygon()
    display()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Filled Polygon")
glutDisplayFunc(main)
glutIdleFunc(main)
glutMainLoop()



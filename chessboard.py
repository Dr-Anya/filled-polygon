import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

colour = 0;
def init():
    glClearColor(0, 1, 1, 0) #display window colour
    glMatrixMode(GL_PROJECTION) #choosing type of projection
    gluOrtho2D(0, 800, 0, 600) #setting transformation as 2D

def square(x1, y1, x2, y2, x3, y3, x4, y4):
    if (colour == 0) {
        glColor3f(1, 1, 1) #draw a white box
        colour = 1 #change colour value to 1
        } else {
            glColor3f(0, 0, 0) #draw a black box
            colour = 0 #change colour value to 0
            }

    glBegin(GL_POLYGON)
    glVertex2i(x1, y1)
    glVertex2i(x2, y2)
    glVertex2i(x3, y3)
    glVertex2i(x4, y4)
    glEnd()

def chessboard():
    glClear(GL_COLOR_BUFFER_BIT)
    x, y
    for (x = 0, x <= 800, x += 100){
        for (y = 0, y <= 600, y += 75){
            square(x, y + 75, x + 100, y + 75, x + 100, y, x, y)
            }
        }
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Chess board")
    init()
    glutDisplayfunc(chessboard)
    glutMainLoop()


main()



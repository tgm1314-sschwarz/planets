

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from Sphere import *

def main():
    pygame.init()
    display = (1600, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # camera settings
    gluPerspective(30, (display[0]/display[1]), 1, 50.0)
    glTranslatef(0.0, 0.0, -10.0)

    # planet1
    p1pos = (0.0, 0.0, 0.0)
    p1 = Sphere(1.0, 40, 40, p1pos)
    p1.position()

    # planet2
    glTranslatef(1,0,0)
    p2pos = (3.0, 0.0, 0.0)
    p2 = Sphere(2.0, 25, 25, p2pos)


    # sun
    #sunpos = (0.0, 0.0, 0.0)
    #sun = Sphere(1.0, 25, 25, sunpos)
    #sun.position()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    p1.rotate += 1
                if event.key == pygame.K_DOWN:
                    p1.rotate -= 1
                if event.key == pygame.K_LEFT:
                    # glTranslatef(1.0, 1.0, 1.0)
                    pass
                if event.key == pygame.K_RIGHT:
                    # glTranslatef(1.0, 1.0, -1.0)
                    pass

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        p1.draw_sphere()
        p1.light()
        glRotatef(p1.rotate, 1, 1, 1)

        p2.draw_sphere()
        p2.light()

        #sun.draw_sphere()
        #sun.light()

        # repaint
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()

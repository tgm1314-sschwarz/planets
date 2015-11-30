import pygame
from pygame.locals import *
from OpenGL.GLUT import *

from _research.Sphere import *
from LoadImages import *

__author__ = 'Gala & Schwarz'


def main():
    pygame.init()
    display = (1600, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glShadeModel(GL_SMOOTH)
    glClearColor(.0, .0, .0, .0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)

    gluPerspective(30, (display[0]/display[1]), 1, 50.0)
    glTranslatef(.0, 0.0, -5.0)
    glRotatef(270, 1, 0, 0)

    rotate = 1

    glMatrixMode(GL_MODELVIEW)

    glutInit()

    i = Image()
    texture = i.load("../pics/earthmap.jpg")

    q = gluNewQuadric()
    p1 = Sphere(1.0, 30, 30, q)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rotate += 1
                if event.key == pygame.K_DOWN:
                    rotate -= 1
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotatef(rotate, .0, .0, 1.0)

        # glDisable(GL_LIGHTING)
        i.place_image(texture)
        # glutSolidSphere(1.0, 30, 30)
        # p1.draw_sphere()
        p1.draw_sphere2()
        # p1.light()

        # repaint
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()

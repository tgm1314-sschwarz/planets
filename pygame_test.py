import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#http://stackoverflow.com/questions/7687148/drawing-sphere-in-opengl-without-using-glusphere


verticies = (
    (0, 0.5, 0),
    (0.5, 0, 0),
    (0, 0, -0.5),
    (0, 0, 0.5),
    (-0.5, 0, 0),
    (0, -0.5, 0),
)

edges = (
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
    (1, 2),
    (1, 3),
    (4, 2),
    (4, 3),
)


def draw_sphere():
    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])

    glEnd()


def main():
    pygame.init()
    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45.0, (display[0]/display[1]), 1, 50.0)

    glTranslatef(0.0, 0.0, -5.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_sphere()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()

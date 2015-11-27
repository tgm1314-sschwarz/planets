import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def main():

    # window Position
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 100)

    pygame.init()

    display = (1600, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Solarsysten, Gala & Schwarz")

    glShadeModel(GL_SMOOTH)
    glClearColor(.0, .0, .0, .0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)

    gluPerspective(50, (display[0]/display[1]), 1, 50.0)
    glTranslatef(.0, .0, -30)

    glMatrixMode(GL_MODELVIEW)

    glutInit()

    while True:
        # getting the mouse position for OpenGL
        x, y = pygame.mouse.get_pos()
        x -= 800
        y -= 450
        #print(x, y)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if x>=-160 and x<=160 and y>=-160 and y<=160:
                    print("oida")

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # drawing a rectangle
        glBegin(GL_QUADS)
        glColor3f(1., .0, .0)
        glVertex2f(-5, 5)
        glVertex2f(-5, -5)
        glVertex2f(5, -5)
        glVertex2f(5, 5)
        glEnd()

        # Redrawing everything
        pygame.display.flip()

        # Delay
        pygame.time.wait(10)

if __name__ == '__main__':
    main()

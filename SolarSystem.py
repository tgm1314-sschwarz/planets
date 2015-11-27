from pygame.locals import *
from Lighting import *
from Animate import *
from Controller import *
from OpenGL.GLUT import *

__author__ = 'Gala & Schwarz'


def main():

    # window Position
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 100)

    # starting pygame
    pygame.init()

    # making a pygame window
    display = (1600, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Solarsysten, Gala & Schwarz")

    glShadeModel(GL_SMOOTH)
    glClearColor(.0, .0, .0, .0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)

    gluPerspective(75, (display[0]/display[1]), 1, 50.0)
    glTranslatef(.0, 6.0, -30)
    glRotatef(45.0, 1.0, .0, .0)

    glMatrixMode(GL_MODELVIEW)

    glutInit()

    # set up the light
    Lighting()

    # starting to animate
    Animate()


if __name__ == '__main__':
    main()

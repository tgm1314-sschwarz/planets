from pygame.locals import *

from planets.factory.SolarSystem import *

__author__ = 'Gala & Schwarz'


def main():
    """
    Function that initiates a PyGame window and the first perspective. Then it starts the animation of the Solar System.
    """

    # window Position
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 50)

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

    gluPerspective(75, (display[0]/display[1]), 1., 100.)

    glMatrixMode(GL_MODELVIEW)

    glutInit()

    # set up the light
    Lighting()

    # starting to animate
    a = SolarSystem()
    a.animation()

if __name__ == '__main__':
    main()

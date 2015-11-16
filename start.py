from pygame import *
from pygame.locals import *
from Sphere import *


def main():
    pygame.init()
    display = (1600, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glLoadIdentity()
    gluPerspective(30, (display[0]/display[1]), 1, 50.0)

    glTranslatef(0.0, 2.0, -30.0)
    glRotatef(35.0, 1.0, 0.0, 0.0)

    # sun
    sun = Sphere(2.0, 40, 40)
    # planet1
    p1 = Sphere(0.7, 25, 25)
    # planet2
    p2 = Sphere(0.7, 25, 25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    p1.rotate += 1
                if event.key == pygame.K_DOWN:
                    p1.rotate -= 1

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotatef(1.0, 0.0, 1.0, 0.0)

        # draw sun
        glColor3f(1.0, 1.0, 0.0)
        sun.draw_sphere2()
        # sun.light2()

        # draw planet 1
        glPushMatrix()
        glTranslatef(10.0, 0.0, 0.0)
        # glRotatef(1.0, 0.0, 1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        p1.draw_sphere()
        glPopMatrix()

        # draw planet 2
        glPushMatrix()
        glTranslatef(-10.0, 0.0, 0.0)
        # glRotatef(3.0, 0.0, 1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        p2.draw_sphere()
        glPopMatrix()

        # repaint
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()

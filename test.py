from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from logging import warning
sphere_locations = [(0, 0)]


def init():
    glClearColor(0., 0., 0., 1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    # glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 550.0, 550.0, 0.0, -100.0, 100.0)
    glEnable(GL_DEPTH_TEST)


def on_click(button, state, x, y):
    global sphere_locations
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        sphere_locations.append((x, y))

def light():
    sun1 = (0.0, 2.0, -1.0, 1.0)
    sun2 = (0.7, 0.7, 0.7, 1.0)
    intense = (0.3, 0.3, 0.3, 1.0)

    glEnable(GL_LIGHTING)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, intense)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, sun1)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, sun2)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

def display():
    global sphere_locations
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for x, y in sphere_locations:
        glPushMatrix()
        glTranslatef(x, y, 1.0)
        light()
        glutSolidSphere(15, 250, 250)
        glRotate(45, 1, 1, 1)
        glPopMatrix()
    glFlush()
    glutSwapBuffers()
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(550, 550)
glutInitWindowPosition(50, 50)
glutCreateWindow(b"Bubble Pop")
glutDisplayFunc(display)
glutMouseFunc(on_click)
init()
glutMainLoop()

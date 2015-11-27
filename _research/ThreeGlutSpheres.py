import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def animate():
    # These three variables control the animation's state and speed.
    hourofday = 1.0
    dayofyear = 365.0
    animateincrement = 24.0

    # Clear the redering window
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    hourofday += animateincrement
    dayofyear += animateincrement/24.0

    hourofday -= (int(hourofday/24))*24
    dayofyear -= (int(dayofyear/365))*365

    # Clear the current matrix (Modelview)
    glLoadIdentity()

    # Back off eight units to be able to view from the origin.
    glTranslatef(0.0, 0.0, -20.0)

    # Rotate the plane of the elliptic
    # (rotate the model's plane about the x axis by fifteen degrees
    glRotatef(15.0, 1.0, 0.0, 0.0)

    # Draw the sun	-- as a yellow, wireframe sphere
    glColor3f(1.0, 1.0, 0.0)
    glutSolidSphere(1.0, 15, 15)

    # Draw the Earth
    # First position it around the sun
    # Use DayOfYear to determine its position
    glRotatef(360.0*dayofyear/365.0, 0.0, 1.0, 0.0)
    glTranslatef(4.0, 0.0, 0.0)
    glPushMatrix()
    #  Second, rotate the earth on its axis
    #  Use HourOfDay to determine its rotation.
    glRotatef(360.0*hourofday/24.0, 0.0, 1.0, 0.0)

    # Third, draw the earth as a wireframe sphere
    glColor3f(0.2, 0.2, 1.0)
    glutWireSphere(0.4, 10, 10)
    glPopMatrix()

    # Draw the moon.
    # Use DayOfYear to control its rotation around the earth
    glRotatef(360.0*12.0*dayofyear/365.0, 0.0, 1.0, 0.0)
    glTranslatef(0.7, 0.0, 0.0)
    glColor3f(0.3, 0.7, 0.3)
    glutWireSphere(0.1, 5, 5)

    # Flush the pipeline, and swap the buffers
    glFlush()
    glutSwapBuffers()

    glutPostRedisplay()		# Request a re-draw for animation purposes


# Initialize OpenGL's rendering modes
def open_gl_init():
    glShadeModel(GL_FLAT)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)


# ResizeWindow is called when the window is resized
def resize_window(w, h):
    if h == 0:
        h = 1
    if w == 0:
        w = 1
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, float(w)/float(h), 1, 50.0)

    glMatrixMode(GL_MODELVIEW)


def main():
    # Need to double buffer for animation
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    # Create and position the graphics window
    glutInitWindowPosition(500, 200)
    glutInitWindowSize(1600, 900)
    glutCreateWindow(b"Solar System Demo")

    # Initialize OpenGL.
    open_gl_init()

    # Set up the callback function for resizing windows
    glutReshapeFunc(resize_window)

    # Callback for graphics image redrawing
    glutDisplayFunc(animate)

    # Start the main loop.  glutMainLoop never returns.

    glutMainLoop()

    return 0

if __name__ == '__main__':
    main()

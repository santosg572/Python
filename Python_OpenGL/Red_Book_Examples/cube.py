from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init(): 
   glClearColor (0.0, 0.0, 0.0, 0.0);
   glShadeModel (GL_FLAT);

def display():
   glClear (GL_COLOR_BUFFER_BIT);
   glColor3f (1.0, 1.0, 1.0);
   glLoadIdentity ();             
   gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
   glScalef (1.0, 2.0, 1.0);      
   glutWireCube (1.0);
   glFlush ();

def reshape (w, h):
   glViewport (0, 0, w, h); 
   glMatrixMode (GL_PROJECTION);
   glLoadIdentity ();
   glFrustum (-1.0, 1.0, -1.0, 1.0, 1.5, 20.0);
   glMatrixMode (GL_MODELVIEW);

#def keyboard(key1, x, y):
#   match key1:
#      case 27:
#         exit;
#         break;

glutInit();
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
glutInitWindowSize (500, 500); 
glutInitWindowPosition (100, 100);
glutCreateWindow (0);
init ();
glutDisplayFunc(display); 
glutReshapeFunc(reshape);
#glutKeyboardFunc(keyboard);
glutMainLoop();

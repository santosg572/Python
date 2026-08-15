import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the 8 corner vertices of a cube
vertices = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1),  (1, 1, 1),  (-1, -1, 1),  (-1, 1, 1)
)

# Connect the vertices to form 12 structural edges
edges = (
    (0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
    (6,3), (6,4), (6,7), (5,1), (5,4), (5,7)
)

def Cube():
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)  # White lines
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL 3D Rotating Cube")

    # Set up 3D Perspective: (FOV, Aspect Ratio, Z-Near, Z-Far)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    
    # Move the camera backward along the Z-axis to see the cube
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Rotate the scene: (Angle in degrees, X, Y, Z vector components)
        glRotatef(1, 3, 1, 1)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()


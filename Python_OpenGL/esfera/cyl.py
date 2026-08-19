import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def generate_sphere(radius, stacks, slices):
    vertices = []
    # Generación de vértices usando las ecuaciones métricas de la esfera
    for i in range(stacks + 1):
        theta = i * np.pi / stacks  # De 0 a PI
        for j in range(slices + 1):
            phi = j * 2 * np.pi / slices  # De 0 a 2*PI
            
            x = radius * np.cos(phi)   #radius * np.sin(theta) * np.cos(phi)
            y = theta  # radius * np.cos(theta)
            z = radius * np.sin(phi)   # radius * np.sin(theta) * np.sin(phi)
            vertices.append((x, y, z))
            
    # Generación de índices para dibujar la malla en modo de cuadrícula (Wireframe)
    indices = []
    for i in range(stacks):
        for j in range(slices):
            first = (i * (slices + 1)) + j
            second = first + slices + 1
            
            indices.extend([first, second, second + 1, first, second + 1, first + 1])
            
    return np.array(vertices, dtype=np.float32), np.array(indices, dtype=np.uint32)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Esfera 3D Paramétrica")

    # Configuración de perspectiva y cámara
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)

    # Generar geometría: radio = 1.5, 20 divisiones verticales, 20 horizontales

    vertices, indices = generate_sphere(.5, 10, 20)

    # Modo de dibujo en malla/líneas para apreciar la geometría esférica
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glEnable(GL_DEPTH_TEST)

    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Rotación continua para visualizar el volumen 3D
        glRotatef(1, 1, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Renderizado mediante arreglos de vértices
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices)
        glColor3f(0.2, 0.8, 1.0)  # Color azul claro
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)
        glDisableClientState(GL_VERTEX_ARRAY)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()


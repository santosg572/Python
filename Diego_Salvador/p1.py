import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# ============================================================
# 1. CONFIGURACIÓN DEL CILINDRO
# ============================================================

radio = 2.0

altura = 5.0

segmentos = 8

anillos = 2

vertices = []

# Guardaremos también los números de vértice de cada anillo.
#
# Esto nos ayudará posteriormente a saber qué vértices
# pertenecen a cada anillo.
anillos_vertices = []


# Distancia vertical entre cada anillo.

dz = altura / anillos


# Número que tendrá el siguiente vértice.

numero_vertice = 0


for i in range(anillos + 1):

    # Calcular la posición vertical del anillo
    # Si altura = 5 y tenemos 2 divisiones:
    # z = -2.5
    # z = 0
    # z = 2.5

    z = -altura / 2 + i * dz


    # Lista para guardar los vértices de este anillo.

    vertices_anillo = []

    pares = []

    for j in range(0, segmentos, 2):

        # Ángulo alrededor del cilindro.
        #
        # El cilindro completa una vuelta de:
        #
        # 0 -> 2π
        #
        theta = 2 * np.pi * j / segmentos


        # Coordenadas del punto sobre el círculo.

        x = radio * np.cos(theta)

        y = radio * np.sin(theta)


        # Guardamos la posición del vértice.

        vertices.append((x, y, z))


        # Guardamos el número del vértice.

        pares.append(numero_vertice)

        vertices_anillo.append(numero_vertice)

        numero_vertice += 1

    impares = []

    for j in range(1, segmentos, 2):

        # Ángulo correspondiente al vértice.

        theta = 2 * np.pi * j / segmentos


        # Coordenadas del punto.

        x = radio * np.cos(theta)

        y = radio * np.sin(theta)


        # Guardamos el vértice.

        vertices.append((x, y, z))


        # Guardamos su número.

        impares.append(numero_vertice)

        vertices_anillo.append(numero_vertice)

        numero_vertice += 1


    # Guardamos la información del anillo.

    anillos_vertices.append({
        "pares": pares,
        "impares": impares
    })


# Convertimos la lista a NumPy.

vertices = np.array(vertices, dtype=np.float32)


# ============================================================
# 3. MOSTRAR LOS VÉRTICES
# ============================================================

print("=" * 60)
print("VÉRTICES GENERADOS")
print("=" * 60)

for i, vertice in enumerate(vertices):

    x, y, z = vertice

    print(
        f"V{i:02d} = "
        f"({x:7.3f}, {y:7.3f}, {z:7.3f})"
    )


# ============================================================
# 4. MOSTRAR LA ESTRUCTURA DE CADA ANILLO
# ============================================================

print("\n")
print("=" * 60)
print("ESTRUCTURA DE LOS ANILLOS")
print("=" * 60)


for i, anillo in enumerate(anillos_vertices):

    print(f"\nANILLO {i}")

    print("Pares: ", anillo["pares"])

    print("Impares: ", anillo["impares"])


triangulos = []


# Número de vértices que tenemos alrededor del cilindro.

# segmentos = 8
#
# Por lo tanto tenemos 8 posiciones angulares.


for i in range(anillos):

    # Anillo inferior
    anillo_actual = anillos_vertices[i]

    # Anillo superior
    anillo_siguiente = anillos_vertices[i + 1]


    # --------------------------------------------------------
    # Para trabajar con los vértices físicamente ordenados
    # alrededor del círculo, reconstruimos la secuencia:
    #
    # 0,1,2,3,4,5,6,7
    #
    # utilizando los pares e impares.
    # --------------------------------------------------------

    actual_ordenado = []

    siguiente_ordenado = []


    # Recuperar pares e impares.

    pares_actual = anillo_actual["pares"]

    impares_actual = anillo_actual["impares"]

    pares_siguiente = anillo_siguiente["pares"]

    impares_siguiente = anillo_siguiente["impares"]


    # --------------------------------------------------------
    # Reconstruir el orden angular:
    #
    # par, impar, par, impar...
    #
    # Ejemplo:
    #
    # 0, 1, 2, 3, 4, 5, 6, 7
    #
    # --------------------------------------------------------

    for k in range(len(pares_actual)):

        actual_ordenado.append(pares_actual[k])

        actual_ordenado.append(impares_actual[k])

        siguiente_ordenado.append(pares_siguiente[k])

        siguiente_ordenado.append(impares_siguiente[k])


    # ========================================================
    # CONSTRUIR LOS TRIÁNGULOS
    # ========================================================
    #
    # Cada posición angular se conecta con la siguiente.
    #
    # También debemos conectar la última posición con
    # la primera para cerrar el cilindro.
    #
    # ========================================================

    for j in range(segmentos):

        siguiente_j = (j + 1) % segmentos


        # Vértices del cuadrilátero actual.

        v0 = actual_ordenado[j]

        v1 = actual_ordenado[siguiente_j]

        v2 = siguiente_ordenado[j]

        v3 = siguiente_ordenado[siguiente_j]


        # ----------------------------------------------------
        # Primer triángulo
        # ----------------------------------------------------
        #
        # v0 -------- v1
        # | /
        # | /
        # | /
        # | /
        # v2
        #
        # ----------------------------------------------------

        triangulos.append(
            (v0, v2, v1)
        )


        # ----------------------------------------------------
        # Segundo triángulo
        # ----------------------------------------------------
        #
        # v0 -------- v1
        # / |
        # / |
        # / |
        # / |
        # v2 ------- v3
        #
        # ----------------------------------------------------

        triangulos.append(
            (v1, v2, v3)
        )


# ============================================================
# MOSTRAR LOS TRIÁNGULOS
# ============================================================

print("\n")
print("=" * 60)
print("TRIÁNGULOS DE LA MALLA")
print("=" * 60)


for i, triangulo in enumerate(triangulos):

    v0, v1, v2 = triangulo

    print(
        f"T{i:02d} = "
        f"(V{v0}, V{v1}, V{v2})"
    )


# ============================================================
# CONVERTIR LOS TRIÁNGULOS EN UNA MATRIZ
# ============================================================

indices = np.array(
    triangulos,
    dtype=np.uint32
)


print("\n")
print("=" * 60)
print("MATRIZ DE ÍNDICES")
print("=" * 60)

print(indices)


# ============================================================
# VISUALIZACIÓN 3D
# ============================================================
#
# Ahora vamos a representar:
#
# - Los vértices
# - Los números de los vértices
# - Las conexiones
# - Los triángulos
#
# Esto permite observar visualmente cómo los índices
# construyen la geometría.
# ============================================================


fig = plt.figure(figsize=(12, 9))

ax = fig.add_subplot(111, projection="3d")


# ============================================================
# DIBUJAR LOS TRIÁNGULOS
# ============================================================

caras = []


for triangulo in triangulos:

    v0, v1, v2 = triangulo

    cara = [
        vertices[v0],
        vertices[v1],
        vertices[v2]
    ]

    caras.append(cara)


# Crear la colección de triángulos.

malla = Poly3DCollection(
    caras,
    alpha=0.35,
    edgecolor="black"
)


ax.add_collection3d(malla)


# ============================================================
# DIBUJAR LOS VÉRTICES
# ============================================================

x = vertices[:, 0]

y = vertices[:, 1]

z = vertices[:, 2]


ax.scatter(
    x,
    y,
    z,
    s=50
)


# ============================================================
# ENUMERAR LOS VÉRTICES
# ============================================================

for i, vertice in enumerate(vertices):

    x, y, z = vertice

    ax.text(
        x,
        y,
        z,
        f"V{i}",
        fontsize=9
    )


# ============================================================
# DIBUJAR LAS CONEXIONES DE LOS TRIÁNGULOS
# ============================================================
#
# Aunque Poly3DCollection ya muestra las caras,
# dibujamos también explícitamente las aristas para
# poder observar las conexiones.
# ============================================================


for triangulo in triangulos:

    v0, v1, v2 = triangulo

    puntos = [
        vertices[v0],
        vertices[v1],
        vertices[v2],
        vertices[v0]
    ]

    puntos = np.array(puntos)

    ax.plot(
        puntos[:, 0],
        puntos[:, 1],
        puntos[:, 2],
        linewidth=1
    )


# ============================================================
# CONFIGURACIÓN DEL GRÁFICO
# ============================================================

ax.set_title(
    "Cilindro 3D: Vértices, Triángulos y Malla"
)

ax.set_xlabel("X")

ax.set_ylabel("Y")

ax.set_zlabel("Z")


# Mantener proporciones aproximadamente iguales.

ax.set_box_aspect((1, 1, altura / radio))


plt.show()


# ============================================================
# RESUMEN DE LA GEOMETRÍA
# ============================================================

print("\n")
print("=" * 60)
print("RESUMEN")
print("=" * 60)

print(f"Número total de vértices: {len(vertices)}")

print(f"Número total de triángulos: {len(triangulos)}")

print(f"Vértices por anillo: {segmentos}")

print(f"Número de anillos: {anillos + 1}")


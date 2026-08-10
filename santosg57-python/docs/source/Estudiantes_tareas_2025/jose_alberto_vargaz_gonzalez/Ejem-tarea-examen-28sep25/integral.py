import numpy as np


def mostrar_resolucion_analitica():
    """
    resolución analítica de la integral
    """
    print("RESOLUCIÓN ANALÍTICA:")
    print("∫₋₁³ [4 - (x - 1)²] dx")
    print()
    print("Paso 1: Expandir la expresión:")
    print("4 - (x - 1)² = 4 - (x² - 2x + 1) = -x² + 2x + 3")
    print()
    print("Paso 2: Integrar término por término:")
    print("∫(-x² + 2x + 3) dx = -x³/3 + x² + 3x + C")
    print()
    print("Paso 3: Evaluar en los límites de integración:")
    print("En x = 3:  -27/3 + 9 + 9 = -9 + 9 + 9 = 9")
    print("En x = -1: -(-1)³/3 + (-1)² + 3(-1) = 1/3 + 1 - 3 = -5/3")
    print()
    print("Paso 4: Calcular la integral definida:")
    print("Resultado = 9 - (-5/3) = 9 + 5/3 = 27/3 + 5/3 = 32/3")
    print()
    print(f"VALOR EXACTO DE LA INTEGRAL: 32/3 ≈ {32/3:.8f}")
    print()

    

def main():
    # Mostrar resolución analítica
    mostrar_resolucion_analitica()
    
    # Valor exacto de la integral
    valor_exacto = 32/3

if __name__ == "__main__":
    main()

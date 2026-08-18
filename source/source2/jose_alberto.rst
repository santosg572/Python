jose_alberto
============

.. code:: Python

   import numpy as np

   # Datos
   x = np.array([1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00])
   y = np.array([1.23, 2.13, 1.42, -0.69, 4.29, 3.64, 9.30, 10.62, 7.42, 8.40, 12.30, 10.30])

   # Paso 1: Calcular sumatorias
   n = len(x)
   sum_x = np.sum(x)
   sum_y = np.sum(y)
   sum_xy = np.sum(x * y)
   sum_x2 = np.sum(x**2)

   # Paso 2: Calcular promedios
   x_mean = sum_x / n
   y_mean = sum_y / n
   print(f"\nPromedios:")
   print(f"x̄ = {x_mean:.2f}")
   print(f"ȳ = {y_mean:.2f}")

   # Paso 3: Calcular β₁ (pendiente)
   numerador_beta1 = sum_xy - n * x_mean * y_mean
   denominador_beta1 = sum_x2 - (sum_x**2) / n
   beta_1 = numerador_beta1 / denominador_beta1

   print(f"\nCálculo de β₁:")
   print(f"Numerador = ∑xy - n·x̄·ȳ = {sum_xy:.2f} - {n}×{x_mean:.2f}×{y_mean:.6f} = {numerador_beta1:.6f}")
   print(f"Denominador = ∑x² - (∑x)²/n = {sum_x2:.0f} - ({sum_x:.0f})²/{n} = {denominador_beta1:.6f}")
   print(f"β₁ = {numerador_beta1:.6f} / {denominador_beta1:.6f} = {beta_1:.6f}")

   # Paso 4: Calcular β₀ (intercepto)
   beta_0 = y_mean - beta_1 * x_mean
   print(f"\nCálculo de β₀:")
   print(f"β₀ = ȳ - β₁·x̄ = {y_mean:.6f} - {beta_1:.6f}×{x_mean:.2f} = {beta_0:.6f}")

   # Resultado final
   print(f"\n=== RESULTADO FINAL ===")
   print(f"β₀ = {beta_0:.6f} ≈ {beta_0:.3f}")
   print(f"β₁ = {beta_1:.6f} ≈ {beta_1:.3f}")
   print(f"Ecuación de la recta: y = {beta_0:.6f} + {beta_1:.6f}x")

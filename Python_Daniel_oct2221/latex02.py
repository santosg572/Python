from sympy import symbols, latex, sympify
from IPython.display import display, Math

x, y, z = symbols('x y z')
equation = 1 + 2**(x + y + z)
latex_output = latex(equation)
print(latex_output)

# In Jupyter, you could display it rendered:
# display(Math(latex_output))



from sympy import symbols, latex, sympify
from IPython.display import display, Math

x, y, mu, varphi = symbols('x y \mu, \varphi)

equation = varphi_{\mu, \sigma^2} (x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{- \frac{(x-\mu)^2}{2 \sigma^2}}

latex_output = latex(equation)
print(latex_output)

# In Jupyter, you could display it rendered:
# display(Math(latex_output))



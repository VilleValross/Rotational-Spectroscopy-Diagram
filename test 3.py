import numpy as np
import matplotlib.pyplot as plt


# Definiera funktionen för ekvationen
def f(x):
    return np.sin(x) + 1

# Skapa en array med x-värden från -5 till 5
x_vals = np.linspace(-10, 10, 100)

# Beräkna motsvarande y-värden för varje x-värde
y_vals = f(x_vals)

# Rita grafen
plt.plot(x_vals, y_vals)

# Visa grafen
plt.show()

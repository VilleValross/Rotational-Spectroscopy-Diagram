import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import RANSACRegressor

# Be användaren mata in antalet punkter
num_points = int(input("Ange antalet punkter: "))

# Skapa en tom array för att lagra punkterna
points = np.empty((num_points, 2))

# Loopa genom alla punkter och be användaren mata in x- och y-koordinaterna
for i in range(num_points):
    x = float(input("Ange x-koordinat för punkt {}: ".format(i+1)))
    y = float(input("Ange y-koordinat för punkt {}: ".format(i+1)))
    points[i] = [x, y]

# Skapa en RANSAC-regressor för att passa en linje till punkterna
model = RANSACRegressor()

# Passa modellen till punkterna
model.fit(points[:, 0].reshape(-1, 1), points[:, 1].reshape(-1, 1))

# Hämta lutningen och skärningen för den passade linjen
slope = model.estimator_.coef_[0][0]
intercept = model.estimator_.intercept_[0]

# Skriv ut ekvationen för den passade linjen
print(f"y = {slope}x + {intercept}")

# Plotta punkterna och medianlinjen
plt.scatter(points[:, 0], points[:, 1])
x_vals = np.array([points[:, 0].min(), points[:, 0].max()])
y_vals = slope * x_vals + intercept
plt.plot(x_vals, y_vals, color='r')

# Visa grafen
plt.show()

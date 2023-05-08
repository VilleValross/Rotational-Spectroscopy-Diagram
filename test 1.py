import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import RANSACRegressor

# Skapa en mängd punkter med slumpmässiga x- och y-koordinater
points = np.random.rand(100, 2)

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

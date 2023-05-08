import matplotlib.pyplot as plt

# Skapa data för x- och y-koordinaterna
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Rita linjediagrammet
plt.plot(x, y)

# Ange etiketter för axlarna och titel för diagrammet
plt.xlabel('X-axel')
plt.ylabel('Y-axel')
plt.title('Linjediagram')

# Visa diagrammet
plt.show()

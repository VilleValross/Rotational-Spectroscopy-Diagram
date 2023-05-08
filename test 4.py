import numpy as np
import matplotlib.pyplot as plt

# Skapa data för Nu/gu, Eu, Ntot och Qrot
Nu_gu = np.array([1.5, 1.8, 2.0, 2.2, 2.5])
Eu = np.array([500, 1000, 1500, 2000, 2500])
Ntot = 1e15
Qrot = 1e25
Tex = 10

# Beräkna ln(Nu/gu) och (Eu/Tex)
ln_Nu_gu = np.log(Nu_gu)
Eu_Tex = Eu/Tex

# Beräkna linjär regression med polyfit
slope, intercept = np.polyfit(Eu_Tex, ln_Nu_gu, 1)

# Skapa en linjär ekvation med linjär regression
x = np.linspace(0, np.max(Eu_Tex), 100)
y = slope * x + intercept

# Rita grafen
plt.plot(Eu_Tex, ln_Nu_gu, 'o', label='Data')
plt.plot(x, y, label=f'y={slope:.2f}x+{intercept:.2f}')

# Lägg till titel och axelbeskrivningar
plt.title(r'ln(Nu/gu) mot Eu i ekvationen $ln(Nu/gu) = ln(Ntot/Qrot)-(Eu/Tex)$')
plt.xlabel(r'$Eu/Tex$')
plt.ylabel(r'$ln(Nu/gu)$')

# Lägg till en legend
plt.legend()

# Visa grafen
plt.show()
print("slope = ", slope, "intercept = ", intercept)

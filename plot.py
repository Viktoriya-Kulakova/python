import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.log(x) + np.cos(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('np.log(x) + np.cos(x)')
plt.title('Plot of np.log(x) + np.cos(x)')
plt.show()
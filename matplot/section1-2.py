import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

rec1 = Rectangle((0.5,0), 0.2, 0.8)
rec2 = Rectangle((0.2,0), 0.2, 0.6)

fig, ax = plt.subplots()

ax.add_patch(rec1)
ax.add_patch(rec2)
ax.patches[0].set_facecolor('purple')
ax.patches[1].set_facecolor('#09FF99')

plt.show()


fig1, ax1 = plt.subplots()
x = list(range(5))
y = np.random.randn(5)
ax1.bar(x,y)
plt.show()
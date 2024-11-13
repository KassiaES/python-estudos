import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

np.random.seed(15)

x = np.linspace(1, 40, 10)

y1 = x / (np.random.rand(10)*2)
y2 = x / (np.random.rand(10)*3)

line1 = Line2D(x, y1)
line2 = Line2D(x, y2)

fig, ax = plt.subplots()

ax.add_line(line1)
ax.add_line(line2)

ax.autoscale()
fig

ax.lines

ax.lines[0].set_color('r')

plt.show()
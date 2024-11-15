import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

np.random.seed(15)

x = np.linspace(1, 40, 10)

y1 = x / (np.random.rand(10)*2)
y2 = x / (np.random.rand(10)*3)

line1 = Line2D(x, y1)
line1.set_alpha(0.3)
line2 = Line2D(x, y2)
line2.set_linestyle('dashed')
line2.set_marker('*')
line2.set_markersize(20)
line2.set_markerfacecolor('white')

fig, ax = plt.subplots()

ax.add_line(line1)
ax.add_line(line2)

ax.autoscale()
fig.set_size_inches(15,5)

ax.lines[0].set_color('r')
ax.set_title('Algum gráfico')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')

plt.show()
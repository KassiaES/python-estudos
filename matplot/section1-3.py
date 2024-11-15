import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

np.random.seed(14)

x = list(range(1,6))
y = np.linspace(1,10,5)

fig, ax = plt.subplots()

def makeBars(ax, x, y, w):
    for x,y in zip(x,y):
        bar = Rectangle((x,0), w, y)
        ax.add_patch(bar)

makeBars(ax, x, y, 0.4)

ax.autoscale()

fig.set_size_inches(15,5)
fig

ax.set_title('Algum gráfico')
ax.set_xlabel('eixo X')
ax.set_ylabel('eixo Y')

for r in ax.patches:
    r.set_edgecolor('g')
    r.set_ls('dashed')
    r.set_lw(3)
    r.set_hatch('\\')
    r.set_facecolor('c')

sketches = [0, 0.25, 0.5, 0.75, 1]

for r,s in zip(ax.patches, sketches):
    r.set_sketch_params(s)

makeBars(ax, x, y, 0.8)
fig

rec_id = range(10)
zorder = reversed(rec_id)
for r,z in zip(rec_id, zorder):
    ax.patches[r].set_zorder(z)

ax.patches[9].set_clip_on(False)
ax.set_xlim(0, 5.4)
ax.set_ylim(0, 9)
fig

plt.show()

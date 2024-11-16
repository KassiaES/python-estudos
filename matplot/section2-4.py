# import pyplot
import matplotlib.pyplot as plt

# Import legend artist
from matplotlib.legend import Legend
from matplotlib.patches import Rectangle

rec1 = Rectangle((0.1, 0), 0.1, 0.3, label='Day 1')
rec2 = Rectangle((0.25, 0), 0.1, 0.6, label='Day 2')
rec3 = Rectangle((0.4, 0), 0.1, 0.9, label='Day 3')

fig, ax = plt.subplots(figsize=(12,4))


ax.add_patch(rec1)
ax.add_patch(rec2)
ax.add_patch(rec3)


colors=['red','green','black']

for p, c in zip(ax.patches, colors):
    p.set_color(c)

handles, labels = ax.get_legend_handles_labels()

legend = Legend(ax, handles = handles, labels=labels)

ax.add_artist(legend)

legend.texts[1].set(color='b', alpha=0.5)
legend.legend_handles[2].set(facecolor='r', alpha=0.2,)
legend.legendPatch.set_boxstyle('round, pad=0.3, rounding_size=2')
legend.legendPatch.set_facecolor('#FFE0B2')
legend.set_bbox_to_anchor([0.75, 0.9])
fig

plt.show()


from matplotlib.patches import Patch
from matplotlib.lines import Line2D


# instantiate the artists
p1 = Patch(facecolor='r', label='Patch is the Patch')
l1 = Line2D([],[], color='green', label='Line is the Line', marker='o', markersize=10)
l2 = Line2D([],[], color='black', label='Line is the Line', marker='*', markersize=10)


#instantiate  a legend
legend2 = Legend(ax, 
                 handles = [p1, l1, l2], 
                 labels=[p1.get_label(), l1.get_label(), l2.get_label()],
                loc=2, handlelength=0.5)



ax.add_artist(legend2)
ax.legend(handles=[p1, l1, l2])
fig

plt.show()
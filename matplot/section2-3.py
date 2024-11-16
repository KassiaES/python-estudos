import matplotlib.pyplot as plt
from matplotlib.legend import Legend
from matplotlib.patches import Rectangle

rec1 = Rectangle((0.1, 0), 0.1, 0.3, label='Day 1')
rec2 = Rectangle((0.25, 0), 0.1, 0.6, label='Day 2')
rec3 = Rectangle((0.4, 0), 0.1, 0.9, label='Day 3')

fig, ax = plt.subplots()

ax.add_patch(rec1)
ax.add_patch(rec2)
ax.add_patch(rec3)


colors=['red','green','black']

for p, c in zip(ax.patches, colors):
    p.set_color(c)

'''
legend = Legend(ax, handles = [ax.patches[0], ax.patches[1], ax.patches[2]], 
                labels=[ax.patches[0].get_label(),ax.patches[1].get_label(), ax.patches[2].get_label() ])
'''
    
handles, labels = ax.get_legend_handles_labels()

ax.legend(handles=handles, labels=labels) 
ax.legend()

fig

plt.show()
import matplotlib.pyplot as plt

fig, ax= plt.subplots(figsize=(12,4))

ax.get_children()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['bottom'].set_color('red')

ax.spines['left'].set(lw=2,ls='dotted')

ax.set_xlabel('I am')
x_label = ax.xaxis.get_label()
x_label.set_size(20)
x_label.set_fontweight('bold')
x_label.set_color('white')
x_label.set_bbox(dict(facecolor='green', boxstyle='rarrow', edgecolor='red', linestyle='dashed', linewidth=2))
x_label.set_x(0.2)
ax.xaxis.labelpad=20
x_label.set_visible(True)

fig

plt.show()
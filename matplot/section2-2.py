import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.text import Annotation

annot = Annotation("LooK", xy=(0.2, 0.2), xytext=(0.5, 0.8), arrowprops=dict(arrowstyle='->'))

fig, ax = plt.subplots()

txt1 = ax._add_text(annot)

fig.set_size_inches(15,5)
ax.set_title('Alguma anotação')
ax.set_xlabel('rótulo X')
ax.set_ylabel('Rótulo Y')

txt1.set_bbox(dict(facecolor='red', boxstyle='circle, pad=1.5', ls='dashed', lw=2))
txt1.set_size(14)
txt1.set_color('white')

arrow = txt1.arrow_patch
arrow

arrow.set_linewidth(2) 
arrow.set_arrowstyle('-[')
arrow.set_connectionstyle('angle, angleA=-90')
fig

arrow.set_connectionstyle('arc3, rad=-0.5')
fig

plt.show()
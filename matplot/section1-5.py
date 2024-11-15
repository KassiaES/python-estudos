import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.text import Text

txt1 = Text(x=0.5, y=0.5, text='dude')
txt2 = Text(0.2, y=0.2, text='Another dude')

fig, ax= plt.subplots()

t1 = ax._add_text(txt1)
t2 = ax._add_text(txt2)

t1.set_color('red') # Sets font color
t1.set_size(24) # set font size
t1.set_alpha(0.8) # set opacity
t1.set_family('sans-serif') # set font family
t1.set_linespacing(0.2) 
t1.set_rotation(45)
t1.set_style('italic')
t1.set_weight('bold')
t1.set_x(0.4)
t1.set_y(0.8)

t1.set_position((0.3,0.3))
t2.set_position((0.1, 0.1))

ax.figure

t1.set_bbox(dict(facecolor='black', boxstyle='darrow, pad=0.4', alpha=0.7, hatch='o' ))
t1.figure

plt.show()
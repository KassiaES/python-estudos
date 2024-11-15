import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.text import Text

x = list(range(1,10))
y = x

fig, ax = plt.subplots(figsize=(15,5))

def makeFAncyBars( ax, x, y, w):
    for x,y in zip(x,y):
        fbox = FancyBboxPatch((x,0), w, y, boxstyle='round')
        ax.add_patch(fbox)

makeFAncyBars(ax, x, y, 0.3)

ax. autoscale()

box_styles = ['circle','darrow','larrow','rarrow','round4','roundtooth','sawtooth','square','circle','round']
for p,s in zip(ax.patches, box_styles):
    p.set_boxstyle(s)

plt.show()

txt1 = Text(x=0.5, y=0.5, text='dude')
txt2 = Text(0.2, y=0.2, text='Another dude')

fig, ax= plt.subplots()

t1 = ax._add_text(txt1)
t2 = ax._add_text(txt2)

ax.texts[0]

plt.show()
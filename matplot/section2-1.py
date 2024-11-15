import matplotlib.pyplot as plt
from matplotlib.text import Annotation

annot = Annotation('Dude', xy=(0.2,0.2), xytext=(0.5,0.8), arrowprops=dict(width=1))

fig, ax = plt.subplots()

an1 = ax._add_text(annot)

ax.annotate("Some string here", 
            xy=(0.8, 0.8), 
            xytext=(0.8, 0.1), 
            arrowprops=dict(arrowstyle='->', lw=2, color='r') )
fig
plt.show()
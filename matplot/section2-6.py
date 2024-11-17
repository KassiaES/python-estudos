import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = ax.xaxis
y = ax.yaxis

for t in x.get_major_ticks():
    t.label20n = True
    t.label10n = False
    t.tick20n = True
    t.tick10n = False
    
    t.label2.set_color('red')
    t.label2.set_size(14)
    
    t.tick2line.set_marker('o')
    t.tick2line.set_markersize(10)

fig1, ax1 = plt.subplots()

ax1.tick_params(axis='x', 
                reset=True, 
                labelcolor='red', 
                labelsize=14, 
                top='On', 
                labeltop='On', 
                labelbottom='Off', 
                bottom='Off')

fig
plt.show()
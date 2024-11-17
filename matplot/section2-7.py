import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axis([0,11,0,11])

ax.set_xlim(0,12)
ax.set_ylim(0,8)

x = ax.xaxis

from matplotlib.ticker import AutoLocator, MaxNLocator, LinearLocator, MultipleLocator, FixedLocator, NullLocator

auto_ticks = AutoLocator()

max_ticks = MaxNLocator(5)

lin_ticks = LinearLocator(5)

mul_ticks = MultipleLocator(2)

fix_ticks = FixedLocator(locs=[0, 1,4,12])

null_ticks = NullLocator()

x.set_major_locator(auto_ticks)

x.set_major_locator(max_ticks)

x.set_major_locator(lin_ticks)

x.set_major_locator(mul_ticks)



fig
plt.show()
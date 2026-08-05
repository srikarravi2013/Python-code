import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x_plot = 5.0
y_plot = 7.0
z = 6.0

ax.plot(x_plot, y_plot, 'o', color='blue')
ax.plot(x_plot, z, 'o', color='orange')

ax.plot([x_plot, x_plot], [y_plot, z], color='black', linestyle='-')

ax.set_xlabel('X-axis label')
ax.set_ylabel('Y-axis label')
ax.set_title('Plot title')

plt.show()
from matplotlib import pyplot as plt

x1 = [40, 50, 60, 70, 80, 90, 100]

y1 = [40, 50, 60, 70, 80, 90, 100]

plt.plot(x1, y1)

plt.xlabel('X Axis')

plt.ylabel('Y Axis')
plt.savefig('Graph.png')
plt.show()
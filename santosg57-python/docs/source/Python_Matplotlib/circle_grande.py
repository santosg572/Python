import matplotlib.pyplot as plt

fig =  plt.figure()

plt.xlim(-5,5)

cir = plt.Circle((.3,.5),2, color='blue')

fig.add_artist(cir)

plt.ylim(-0.5, 0.5)

plt.show()



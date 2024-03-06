import matplotlib.pyplot as pyplot

def plot_shape(shape, title):
    plt.plot(shape[:, 0], shape[:, 1])
    plt.title(title)
    plt.axis('equal')
    plt.show()

plot_shape(square, 'Original Square')
plot_shape(translated_square, 'Translated Square')
plot_shape(rotated_square, 'Rotated Square')
plot_shape(scaled_square, 'Scaled Square')


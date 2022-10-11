import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(x_low, x_high, y_low, y_high, points_x, points_y):
    """
    Создает изображение множества Мандельброта в диапазоне по x от x_low до x_high,
    по y - от y_low до y_high с разрешением points_x*points_y
    """
    re = np.linspace(x_low, x_high, points_x)
    im = np.linspace(y_low, y_high, points_y).reshape((-1, 1))
    c = re + im * 1j
    z = np.zeros((points_x, points_y))
    z_delta = np.zeros((points_x, points_y))

    for k in range(10):
        z_pr = z.copy()
        z = z ** 2 + c
        z_delta = z - z_pr
    for k in range(100):
        z = z ** 2 + c

    z_delta = np.abs(z_delta)
    mx = 0
    for x in z_delta:
        mx = max(mx, max(x))
    z_delta = z_delta / mx
    img = np.zeros((points_x, points_y))
    # print(z_delta)
    img = (1 - np.log(z_delta * np.exp(1))) * 255
    img[np.abs(z) < 2] = 255

    plt.imshow(img)
    plt.show()
    pass


mandelbrot(-2, 2, -2, 2, 200, 200)
def gaussian_blur(img_array, sigma):
    """
    Выполняет гауссово размытие с заданной дисперсией
    """
    w = np.zeros((9,9))
    for x in range(9):
        for y in range(9):
            w[x,y] = math.exp(-0.5*((x-4)**2+(y-4)**2)/(sigma**2))
    blur(img_array, w)
    pass
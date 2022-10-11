def blur(img_array, weights_array):
    """
    Вычисляет свертку изображения и нормированной весовой матрицы.
    """
    weights_array /= weights_array.sum()
    for x in range(3):
        img_array[:,:,x] = scipy.ndimage.convolve(img_array[:,:,x], weights_array)
        img_array[img_array > 255] = 255
    pass
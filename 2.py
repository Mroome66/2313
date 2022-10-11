import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img = Image.open('flowers.jpg')
img_arr = np.array(img)
ax1 = plt.subplot(221)
modified = img_arr.astype('float')
for x in range(3):
    modified[:, :, x] *= 1.25
    modified[modified > 255] = 255
modified = modified.astype('uint8')
ax1.imshow(modified)
ax2 = plt.subplot(222)
modified = img_arr.astype('float')
modified[:, :, 1] /= 3
modified[modified > 255] = 255
modified = modified.astype('uint8')
ax2.imshow(modified)
ax3 = plt.subplot(223)
ax3.imshow(img_arr[:, :, ::-1])
plt.show()
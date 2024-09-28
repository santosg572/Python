import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_path = "file41.png"


image = mpimg.imread(image_path)

print(image.shape)

image = image[:, :, 1]

print(image.shape)

plt.imshow(image)
plt.show()



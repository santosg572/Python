import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Load a NIfTI file
nifti_img = nib.load('sub-01_T1w.nii.gz')

img = np.zeros((432,432))

image_data = nifti_img.get_fdata()

print(image_data.shape)

sagital = image_data[80,:,:]
#plt.imshow(sagital)

img[0:256,0:256] = sagital

coronal = image_data[:,100,:]
print(coronal.shape)

imgt = np.rot90(coronal)
print(imgt)
 
img[0:256, 256:432] = imgt

#plt.imshow(coronal)

axial = image_data[:,:,100]
print(axial.shape)

img[256:432, 0:256] = axial
#plt.imshow(axial)

plt.imshow(img)
plt.show()




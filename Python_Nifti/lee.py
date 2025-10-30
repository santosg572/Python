import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Load a NIfTI file

file = 'Datos_Curso/sub-01_T1w.nii.gz'

nifti_img = nib.load(file)

print(type(nifti_img))

datosIMG = nifti_img.get_fdata()

print(type(datosIMG))

print(datosIMG.shape)

img = np.zeros((432,432))


sagital = datosIMG[80,:,:]
#sagital = np.rot90(sagital)

img[:256,:256] = sagital

coronal = datosIMG[:,100,:]
coronal = np.rot90(coronal)
print(coronal.shape)

img[:256,256:] = coronal

axial = datosIMG[:,:,100]
print(axial.shape)

img[256:, :256] = axial
plt.imshow(img)
plt.show()

'''
img[256:432, 0:256] = axial
#plt.imshow(axial)


plt.imshow(img)
plt.show()
'''


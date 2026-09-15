import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Load a NIfTI file

pat = "/Users/leopoldogonzalez/cannabis_datos/ds000174-download/"
sujeto = 'sub-101'
dir = 'ses-BL/anat' 
file = 'sub-101_ses-BL_T1w.nii.gz'


file = pat+'/'+sujeto+'/'+dir+'/'+file

nifti_img = nib.load(file)

print(type(nifti_img))

datosIMG = nifti_img.get_fdata()

print(type(datosIMG))

print(np.max(datosIMG))

datosIMG = datosIMG/np.max(datosIMG)

nn = datosIMG.shape


fig, ax = plt.subplots()
im = ax.imshow(datosIMG[0,:,:], cmap='gray')

for k in range(nn[0]):
  sagital = datosIMG[k,:,:]
  im.set_array(sagital)
  plt.draw()
  plt.pause(0.5)  # Pausa de medio segundo entre imágenes

plt.show()



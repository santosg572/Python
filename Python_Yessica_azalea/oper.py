import nibabel as nib
import numpy as np

file1 = 'sub-25an_run02_thresh_zstat6.nii.gz'
file2 = 'sub-26an_thresh_zstat6.nii.gz'
file3 = 'sub-27an_thresh_zstat6.nii.gz'

def LeeIMG(fil99=''):
   # Specify the path to your .nii.gz file
   nifti_file_path = 'c6_cnb/'+fil99
#sub-27an_thresh_zstat6.nii.gz'

   # Load the NIfTI image
   try:
       img = nib.load(nifti_file_path)
       print(f"Successfully loaded: {nifti_file_path}")
   except FileNotFoundError:
       print(f"Error: File not found at {nifti_file_path}")
       exit()
   except Exception as e:
       print(f"An error occurred while loading the NIfTI file: {e}")
       exit()

   # Access the image data as a NumPy array
   data = img.get_fdata() 
   return data

data1 = LeeIMG(file1)
data2 = LeeIMG(file2)    
data3 = LeeIMG(file3)    


print(data1.shape)
print(data1.max())
print(data1.min())

print(data2.shape)
print(data2.max())
print(data2.min())

print(data3.shape)
print(data3.max())
print(data3.min())

dd = data3.shape
print(dd)

datosN = np.zeros(dd)

for i in np.arange(dd[0]):
  for j in np.arange(dd[1]):
    for k in np.arange(dd[2]):
      ma = data1[i,j,k]
      if ma < data2[i,j,k]:
        ma = data2[i,j,k]
      if ma < data3[i,j,k]:
        ma = data3[i,j,k]
      datosN[i,j,k] = ma

img = nib.load('c6_cnb/'+file3)

new_img = nib.Nifti1Image(datosN, affine=img.affine, header=img.header)
nib.save(new_img, 'rescaled_image.nii.gz')        


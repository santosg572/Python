import nibabel as nib
import numpy as np

# Specify the path to your .nii.gz file
nifti_file_path = 'c6_cnb/sub-27an_thresh_zstat6.nii.gz'

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

dd = dir(img)

#print(dd)

for ss in dd:
  if ss[0] != '_':
    print('&&&&&&&&&&&&&&&&&&&&&&&&& ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    print(help(eval('img.'+ss)))



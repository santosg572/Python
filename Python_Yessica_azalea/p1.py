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

# Access the image data as a NumPy array
data = img.get_fdata() 

# Access the image header
header = img.header

# Access the affine transformation matrix
affine = img.affine

# Print some information about the image
print(f"\nImage shape: {data.shape}")
print(f"Data type: {data.dtype}")
print(f"Header info: {header}")
print(f"Affine matrix:\n{affine}")

# You can now work with the 'data' array, which contains the image voxel values.
# For example, to get a slice:
# slice_data = data[:, :, 10] 
# print(f"Shape of a slice: {slice_data.shape}")



Manejo de imágenes de Resonancia Magnética
===========================================

**Manejo de ambientes con ``conda``.**

* conda env list

* conda create -n test_env python=3.10

* conda activate test_env

* conda deactivate

**Instalación de módulo:**

* pip install nibabel

**Ejercicio.**

1. Bajar datos de ``dropbox``

2. Listo primeras instrucciones para leer la imagen.

.. code:: Python

   import nibabel as nib
   import matplotlib.pyplot as plt
   import numpy as np

   # Load a NIfTI file
   
   nifti_img = nib.load('sub-01_T1w.nii.gz')

3. Hacer lo que hay que hacer.




Manejo de imágenes de Resonancia Magnética
===========================================

**Manejo de ambientes con:**  ``conda``

* conda env list

* conda create -n test_env python=3.10

* conda activate test_env

* conda deactivate

**Instalación de módulo:** ``nibabel``

.. code:: Python

   pip install nibabel

**Ejercicio.**

1. Bajar datos de ``dropbox``

`datos <https://www.dropbox.com/scl/fi/4axgbxi67ta40e53i2ya0/sub-01_T1w.nii.gz?rlkey=avy8w0o1ee3a3mu5yg1r8h11w&st=jqa2fqbz&dl=0>`_

2. Listo las primeras instrucciones para leer la imagen de resonancia magnética..

.. code:: Python

   import nibabel as nib
   import matplotlib.pyplot as plt
   import numpy as np

   # Load a NIfTI file
   
   nifti_img = nib.load('sub-01_T1w.nii.gz')

3. Hacer lo que hay que hacer.




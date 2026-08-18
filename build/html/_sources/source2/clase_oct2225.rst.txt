Clase-oct2225
=============

* Tkinter

.. code:: Python

   import tkinter
   root = tkinter.Tk()
   tkinter.mainloop()

Convertir archivi jupyter a python

* pip install nbconvert

.. code:: Python

   jupyter nbconvert --to python notebook.ipynb 

* Lee imágenes de Resonancia Magnética Estructurales

  https://www.dropbox.com/scl/fo/kp0z1x0bmb3oyi42ts2ub/AL99WBdVuNk6pyTTuEXwbpo?rlkey=b5wo8xtv09qkg67nu25i6cx9z&st=i9yhy8z5&dl=0

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






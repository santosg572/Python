Audio
=====

.. code:: Bash

   conda env list
   conda create -n myenv python=3.10

**Play audio**

.. code:: Python


   from playsound import playsound

   playsound('output_scipy.wav')

**Genera audio**

.. code:: Python

   from scipy.io.wavfile import write
   import numpy as np

   sample_rate = 44100  # samples per second
   duration = 3         # seconds

   frequency = 440  # Hz
   t = np.linspace(0., duration, int(sample_rate * duration))
   amplitude = np.iinfo(np.int16).max  # Max value for 16-bit signed integer
   data = amplitude * np.sin(2. * np.pi * frequency * t)

   write("output_scipy.wav", sample_rate, data.astype(np.int16))

   print("WAV file 'output_scipy.wav' created successfully.")




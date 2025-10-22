import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np

# Configura la frecuencia de muestreo y la duración

fs = 44100  # Frecuencia de muestreo en Hz
duration = 10  # Duración de la grabación en segundos

print(f"Grabando durante {duration} segundos...")

# Graba audio en una matriz NumPy
# sd.rec graba el audio y lo almacena en la variable 'record_voice'
# sd.wait se asegura de que la grabación se complete antes de continuar

record_voice = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()

print("record_voice")


print("Grabación finalizada.")

# Guarda el audio grabado en un archivo WAV
# wav.write escribe los datos de audio en el archivo especificado

wav.write('MiGrabacion.wav', fs, record_voice)
print("El audio se guardó como MiGrabacion.wav")



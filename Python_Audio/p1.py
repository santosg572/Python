
import wave

datos = wave.open('salida.wav', 'rb')

ncan = datos.getnchannels()
print(ncan)

samples = datos.getsampwidth()
print(samples)

frec = datos.getframerate()
print(frec)

nframes = datos.getnframes()
print(nframes)

nf = 1000
frames = datos.readframes(nf)

print(frames)






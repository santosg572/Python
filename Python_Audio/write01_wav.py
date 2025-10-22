from scipy.io.wavfile import write
import numpy as np

# Audio parameters
sample_rate = 44100  # samples per second
duration = 10         # seconds

# Generate some sample audio data (e.g., a sine wave)
frequency = 440  # Hz
t = np.linspace(0., duration, int(sample_rate * duration))
amplitude = np.iinfo(np.int16).max  # Max value for 16-bit signed integer
data = np.round(amplitude * np.sin(2. * np.pi * frequency * t))

# Write to the WAV file
write("output_scipy.wav", data, data.astype(np.int16))

print("WAV file 'output_scipy.wav' created successfully.")



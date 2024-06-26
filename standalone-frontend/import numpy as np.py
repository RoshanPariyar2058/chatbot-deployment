import numpy as np
import matplotlib.pyplot as plt

# Given values
x = [1, np.exp(-2), np.exp(-4), np.exp(-6)]
N = 4

# Compute DTFS coefficients
X = np.fft.fft(x) / N

# Compute magnitude and phase spectra
magnitude_spectrum = np.abs(X)
phase_spectrum = np.angle(X)

# Plot the magnitude spectrum
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.stem(range(N), magnitude_spectrum, use_line_collection=True)
plt.title('Magnitude Spectrum')
plt.xlabel('k')
plt.ylabel('|X[k]|')
plt.grid(True)

# Plot the phase spectrum
plt.subplot(1, 2, 2)
plt.stem(range(N), phase_spectrum, use_line_collection=True)
plt.title('Phase Spectrum')
plt.xlabel('k')
plt.ylabel('∠X[k] (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()

magnitude_spectrum, phase_spectrum

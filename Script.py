# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:16:21 2023

@author: nadya
"""

# ID
print("Nama: Nadya P. Arisni")
print("NRP: 5009211079")

import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(frequency, duration, sampling_rate):
    t = np.arange(0, duration, 1/sampling_rate)
    signal = np.sin(2 * np.pi * frequency * t)
    return t, signal

def add_noise(signal, noise_amplitude):
    noise = np.random.normal(0, noise_amplitude, len(signal))
    noisy_signal = signal + noise
    return noisy_signal

def calculate_fft(signal, sampling_rate):
    n = len(signal)
    fft_result = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(n, 1/sampling_rate)
    return frequencies, fft_result

# Parameters
frequency = 5  # Frequency of the sine wave (in Hz)
duration = 1  # Duration of the signal (in seconds)
sampling_rate = 1000  # Sampling rate (in Hz)
noise_amplitude = 0.2  # Amplitude of noise to be added

# Generate a sine wave
t, signal = generate_sine_wave(frequency, duration, sampling_rate)

# Add noise to the sine wave
noisy_signal = add_noise(signal, noise_amplitude)

# Calculate the FFT of the noisy signal
frequencies, fft_result = calculate_fft(noisy_signal, sampling_rate)

# Plot the results
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.title("Original Sine Wave")
plt.plot(t, signal)

plt.subplot(2, 2, 2)
plt.title("Noisy Signal")
plt.plot(t, noisy_signal)

plt.subplot(2, 2, 3)
plt.title("FFT of Noisy Signal")
plt.plot(frequencies, np.abs(fft_result))
plt.xlim(0, sampling_rate/2)

plt.tight_layout()
plt.show()

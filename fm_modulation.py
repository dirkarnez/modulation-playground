import numpy as np

def fm_modulation(carrier_freq, modulating_freq, mod_index, duration, sample_rate):
    """
    Generates a Frequency Modulated (FM) signal.

    Args:
        carrier_freq (float): The frequency of the carrier wave (Hz).
        modulating_freq (float): The frequency of the modulating signal (Hz).
        mod_index (float): The modulation index (beta).
        duration (float): The duration of the signal (seconds).
        sample_rate (int): The number of samples per second.

    Returns:
        numpy.ndarray: The FM signal waveform.
        numpy.ndarray: The time vector.
    """
    t = np.linspace(0., duration, int(sample_rate * duration), endpoint=False)
    
    # Message signal (modulating signal)
    # For a simple sine wave, x(t) = cos(2*pi*modulating_freq*t)
    # The integral of x(t) is (1 / (2*pi*modulating_freq)) * sin(2*pi*modulating_freq*t)
    
    # Calculate the instantaneous phase
    # Phase(t) = 2*pi*fc*t + beta * sin(2*pi*fm*t) where beta is mod_index
    # The term mod_index (beta) can also be seen as (delta_f / fm)
    
    delta_f = mod_index * modulating_freq
    
    # Calculate the instantaneous phase directly using the integrated message signal
    # A * cos(Phase(t))
    fm_signal = np.cos(2 * np.pi * carrier_freq * t + mod_index * np.sin(2 * np.pi * modulating_freq * t))
    
    return fm_signal, t

# Example Usage:
Fc = 1000  # Carrier frequency in Hz
Fm = 100   # Modulating frequency in Hz
Beta = 5   # Modulation Index
D = 1      # Duration in seconds
Fs = 44100 # Sample rate in Hz

fm_wave, time_vec = fm_modulation(Fc, Fm, Beta, D, Fs)

# You can then use libraries like matplotlib to visualize the signal, 
# or sounddevice to play the audio

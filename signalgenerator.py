import numpy as np
# import matplotlib.pyplot as plot

SAMPLE_RATE = 44100
LIMIT_SAMPLE_16B = 32767

def generate_samples(seconds, frequency):
    # define the volumn for the produced sound
    volume = 0.8

    def amplitude(x):
        """
        Makes the value be more 'round'.
        """
        x = x * (2.0 * np.pi * frequency / SAMPLE_RATE)
        x = np.sin(x)
        x = x * LIMIT_SAMPLE_16B
        x = x * volume
        x = np.int16(x)
        return x
    
    required_samples = np.arange(1.0, (seconds/1000 * SAMPLE_RATE))
    samples = map(amplitude, required_samples)
    return np.array(list(samples), dtype=np.int16)

# x = generate_samples(5, 440)
# y = np.sin(x)
# plot.plot(x, y)
# plot.show()
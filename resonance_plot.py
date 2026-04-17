import numpy as np
import matplotlib.pyplot as plt

# 1. Define the frequency ratio range (r = driving_freq / natural_freq)
# We look at r from 0 to 2 to see the peak at 1.0
r = np.linspace(0, 2, 500)

# 2. Define different damping ratios (zeta)
# Low damping (0.1) creates a sharp peak; High damping (0.5) creates a flat peak.
damping_ratios = [0.1, 0.2, 0.5]

plt.figure(figsize=(10, 6))

for zeta in damping_ratios:
    # 3. Resonance Formula: Amplitude response M
    amplitude = 1 / np.sqrt((1 - r**2)**2 + (2 * zeta * r)**2)
    
    plt.plot(r, amplitude, label=f'Damping (ζ) = {zeta}')

# 4. Formatting the Graph
plt.title('Resonance Curve: Amplitude vs. Frequency Ratio', fontsize=14)
plt.xlabel('Frequency Ratio (ω / ω₀)', fontsize=12)
plt.ylabel('Magnification Factor (Amplitude)', fontsize=12)
plt.axvline(x=1.0, color='gray', linestyle='--', label='Natural Frequency')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# 5. Show and Save
plt.show()

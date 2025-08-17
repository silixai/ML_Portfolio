# Convert joules to kilocalories for ML preprocessing
joules = [1000, 4184, 10000, 50000, 100000]
kilocalories = [j * 0.000239 for j in joules]
print(f"Energies in kilocalories: {kilocalories}")

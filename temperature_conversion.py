# Convert Celsius to Fahrenheit for ML preprocessing
celsius = [0, 20, 37, 100, -40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(f"Temperatures in Fahrenheit: {fahrenheit}")

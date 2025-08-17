# Categorize house sizes (square meters) into labels for ML preprocessing
house_sizes = [30, 75, 120, 200, 300]
size_labels = ["Small" if size < 100 else "Medium" if size < 200 else "Large" for size in house_sizes]
print(f"House size labels: {size_labels}")

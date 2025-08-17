# ML Portfolio (SilixAI)
Portfolio of AI/ML projects showcasing preprocessing, feature engineering, and error handling for silixai.com.

## Temperature Conversion
Converts a list of Celsius temperatures to Fahrenheit using a list comprehension. Demonstrates data transformation for ML preprocessing.
- **Input**: List of Celsius temperatures [0, 20, 37, 100, -40]
- **Output**: List of Fahrenheit temperatures [32.0, 68.0, 98.6, 212.0, -40.0]
- **Skills**: Python list comprehensions, data preprocessing

## Distance Conversion
Converts a list of kilometer distances to miles using a list comprehension. Demonstrates data transformation for ML preprocessing under silixai.com.
- **Input**: List of kilometer distances [2, 5, 12, 42.195, 100]
- **Output**: List of mile distances [1.242742, 3.106855, 7.456452, 26.218749, 62.1371]
- **Skills**: Python list comprehensions, data preprocessing

# Energy Conversion
Converts a list of energy values in joules to kilocalories using a list comprehension. Demonstrates data transformation for ML preprocessing under silixai.com.
- **Input**: List of energies in joules [1000, 4184, 10000, 50000, 100000]
- **Output**: List of energies in kilocalories [0.239, 1.0, 2.39, 11.95, 23.9]
- **Skills**: Python list comprehensions, data preprocessing

# Satisfaction Normalization
Normalizes a list of satisfaction scores (0-100) to a 0-1 scale using a list comprehension. Demonstrates data scaling for ML preprocessing under silixai.com.
- **Input**: List of satisfaction scores [10, 25, 50, 75, 100]
- **Output**: List of normalized scores [0.1, 0.25, 0.5, 0.75, 1.0]
- **Skills**: Python list comprehensions, data normalization

# House Size Labeling
Categorizes house sizes (in square meters) into 'Small', 'Medium', or 'Large' using a list comprehension with conditional logic. Demonstrates feature engineering for ML preprocessing under silixai.com.
- **Input**: List of house sizes [30, 75, 120, 200, 300]
- **Output**: List of size labels ['Small', 'Small', 'Medium', 'Large', 'Large']
- **Skills**: Python list comprehensions, conditional logic, feature engineering

# Stock Labeling
Labels price changes for AAPL, TSLA, MSFT, and NVDA as 'Up', 'Down', or 'Stable' based on daily percentage change using a list comprehension and dictionary, using estimated prices around last Friday (Aug 15, 2025). Demonstrates advanced time-series preprocessing for ML under silixai.com.
- **Input**: Stock data {AAPL: [232.00, 231.19], TSLA: [334.00, 330.1501], MSFT: [522.00, 520.35], NVDA: [181.00, 179.74]}
- **Output**: Labels {AAPL: 'Stable', TSLA: 'Down', MSFT: 'Stable', NVDA: 'Stable'} with changes (AAPL: -0.35%, TSLA: -1.15%, MSFT: -0.32%, NVDA: -0.70%)
- **Skills**: Python dictionaries, list comprehensions, conditional logic, time-series preprocessing
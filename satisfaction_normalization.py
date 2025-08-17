# Normalize satisfaction scores (0-100) to 0-1 scale for ML preprocessing
satisfaction_scores = [10, 25, 50, 75, 100]
normalized_scores = [score / 100 for score in satisfaction_scores]
print(f"Normalized satisfaction scores: {normalized_scores}")

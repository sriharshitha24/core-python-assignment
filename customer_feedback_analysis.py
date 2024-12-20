def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available."

    total_ratings = len(ratings)
    positive_ratings = [rating for rating in ratings if rating == 4 or rating == 5]
    positive_percentage = (len(positive_ratings) / total_ratings) * 100

    return f"Positive Feedback: {positive_percentage:.1f}%"

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
result = calculate_positive_feedback_percentage(ratings)
print(result)  
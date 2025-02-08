#Contains all the mathematical functions.

import math as m  # Needed for standard deviation calculation. Imported an m so it's nnot confused with the variable

def calculate_average(scores):
    """Calculate the average of a list of scores."""
    return sum(scores) / len(scores)

def assign_grade(score):
    """Assign a grade based on the score."""
    if score >= 85:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 65:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def calculate_min_max_range(scores):
    """Calculate the minimum, maximum, and range of scores."""
    Min_score = min(scores)
    Max_score = max(scores)
    Score_range = Max_score - Min_score
    return Min_score, Max_score, Score_range

def assign_pass_fail(average):
    """Determine if the student has passed or failed based on the average score."""
    return 'Pass' if average >= 50 else 'Fail'

def calculate_standard_deviation(scores, average):
    """Calculate the standard deviation of a list of scores."""
    variance = sum((x - average) ** 2 for x in scores) / len(scores)
    return m.sqrt(variance)

def rank_subjects(scores):
    """Rank subjects based on scores from highest to lowest."""
    subjects = ['Math', 'Science', 'English']
    sorted_subjects = [sub for _, sub in sorted(zip(scores, subjects), reverse=True)]
    return " > ".join(sorted_subjects)

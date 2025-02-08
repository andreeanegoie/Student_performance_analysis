# Handles reading and writing CSV files.

import csv
import os #The os module in Python  allows me to work with files, directories, environment variables, and system commands.

from calculations import (
    calculate_average, assign_grade, calculate_min_max_range, 
    assign_pass_fail, calculate_standard_deviation, rank_subjects
)

def read_student_data(filename):
    """Read student scores from a CSV file with error handling."""
    students = []
    
    # Check if file exists before trying to open
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return students  # Return an empty list

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header row
            
            for row in reader:
                try:
                    name, math, science, english = row
                    
                    # Convert scores to integers and validate them
                    scores = [int(math), int(science), int(english)]
                    
                    if any(score < 0 or score > 100 for score in scores):  
                        print(f"Warning: Invalid scores for {name}. Skipping entry.")
                        continue  # Skip this entry if scores are invalid

                    # Perform calculations
                    average = calculate_average(scores)
                    math_grade = assign_grade(int(math))
                    science_grade = assign_grade(int(science))
                    english_grade = assign_grade(int(english))
                    min_score, max_score, score_range = calculate_min_max_range(scores)
                    pass_fail_status = assign_pass_fail(average)
                    total_score = sum(scores)
                    std_dev = calculate_standard_deviation(scores, average)
                    subject_ranking = rank_subjects(scores)

                    # Store student data
                    students.append([
                        name, int(math), int(science), int(english),
                        math_grade, science_grade, english_grade,
                        min_score, max_score, score_range,
                        average, pass_fail_status, total_score,
                        round(std_dev, 2), subject_ranking
                    ])
                
                except ValueError:
                    print(f"Warning: Invalid data format in row {row}. Skipping entry.")

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return students

def write_student_results(filename, students):
    """Write processed student data to a CSV file with error handling."""
    if not students:
        print("Error: No student data available to write.")
        return

    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                'Name', 'Math', 'Science', 'English', 
                'Math Grade', 'Science Grade', 'English Grade', 
                'Min Score', 'Max Score', 'Range', 
                'Average', 'Pass/Fail',
                'Total Score', 'Std Dev', 'Subject Ranking'
            ])
            writer.writerows(students)

        print(f'Results saved to {filename}')
    
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

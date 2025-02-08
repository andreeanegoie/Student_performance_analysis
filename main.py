# Handles reading and writing CSV files.

from data_processing import read_student_data, write_student_results

def main():
    input_file = 'Students.csv'
    output_file = 'Student_Results.csv'

    # Read student data from CSV
    students = read_student_data(input_file)
    
    # Write processed student results to CSV
    write_student_results(output_file, students)

if __name__ == '__main__':
    main()

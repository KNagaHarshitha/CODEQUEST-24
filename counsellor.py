import pandas as pd
import random

# Sample data generation
num_entries = 1000

data = {
    'Student ID': [f'{i:03}' for i in range(1, num_entries+1)],
    'Age': [random.randint(18, 24) for _ in range(num_entries)],
    'Gender': [random.choice(['Male', 'Female']) for _ in range(num_entries)],
    'Attendance (%)': [random.randint(50, 100) for _ in range(num_entries)],
    'Avg Exam Score (%)': [random.randint(40, 100) for _ in range(num_entries)],
    'Understanding Level (1-5)': [random.randint(1, 5) for _ in range(num_entries)],
    'Health Issues': [random.choice(['Yes', 'No']) for _ in range(num_entries)],
    'Financial Challenges': [random.choice(['Yes', 'No']) for _ in range(num_entries)],
    'Personal Issues': [random.choice(['Yes', 'No']) for _ in range(num_entries)],
    'Time Management (1-5)': [random.randint(1, 5) for _ in range(num_entries)],
    'Engagement Level (1-5)': [random.randint(1, 5) for _ in range(num_entries)],
    'Learning Environment Quality (1-5)': [random.randint(1, 5) for _ in range(num_entries)],
    'Peer Influence (1-3)': [random.randint(1, 3) for _ in range(num_entries)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to generate solutions for each student
def generate_solutions(row):
    solutions = {
        "Academic Support": [],
        "Personal Well-being": [],
        "Time Management & Engagement": []
    }

    # Academic Support
    if row['Avg Exam Score (%)'] < 60:
        solutions["Academic Support"].append("Provide tutoring in weak subjects.")
    if row['Understanding Level (1-5)'] < 3:
        solutions["Academic Support"].append("Assign additional reading and practice exercises.")
    if row['Attendance (%)'] < 75:
        solutions["Academic Support"].append("Check attendance issues, provide incentives for better attendance.")
    
    # Personal Well-being
    if row['Health Issues'] == 'Yes':
        solutions["Personal Well-being"].append("Encourage regular health check-ups.")
    if row['Personal Issues'] == 'Yes':
        solutions["Personal Well-being"].append("Offer mental health counseling.")
    if row['Financial Challenges'] == 'Yes':
        solutions["Personal Well-being"].append("Provide information about financial aid.")
    
    # Time Management & Engagement
    if row['Time Management (1-5)'] < 3:
        solutions["Time Management & Engagement"].append("Provide time management workshops.")
    if row['Engagement Level (1-5)'] < 3:
        solutions["Time Management & Engagement"].append("Assign engaging group projects.")
    if row['Learning Environment Quality (1-5)'] < 3:
        solutions["Time Management & Engagement"].append("Evaluate and improve learning environment.")
    
    return solutions

# Apply solution generation to each student
df['Tailored Solutions'] = df.apply(generate_solutions, axis=1)

# Print tailored solutions for the first few students as an example
for i in range(5):
    print(f"Student ID: {df['Student ID'][i]}")
    print("Academic Support:")
    for solution in df['Tailored Solutions'][i]['Academic Support']:
        print(f" - {solution}")
    print("Personal Well-being:")
    for solution in df['Tailored Solutions'][i]['Personal Well-being']:
        print(f" - {solution}")
    print("Time Management & Engagement:")
    for solution in df['Tailored Solutions'][i]['Time Management & Engagement']:
        print(f" - {solution}")
    print("\n")

# Save the results to CSV
df.to_csv('student_solutions.csv', index=False)

print("Solutions generated successfully!")

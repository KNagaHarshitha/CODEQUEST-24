import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Define the number of entries
num_entries = 1000

# Generate the dataset
data = {
    'Student ID': [f'{i:03}' for i in range(1, num_entries+1)],
    'Age': [random.randint(18, 24) for i in range(num_entries)],
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
    'Peer Influence (1-5)': [random.randint(1, 5) for _ in range(num_entries)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Save the dataset to CSV (optional, if you want to persist it)
df.to_csv('student_data.csv', index=False)

print("Dataset created successfully")
def create_scatter_plot(x_metric, y_metric):
    plt.figure(figsize=(10, 6))
    
    # Use seaborn for better aesthetics
    sns.scatterplot(data=df, x=x_metric, y=y_metric, hue='Gender', palette='deep', s=100, alpha=0.7)
    
    # Set plot title and labels
    plt.title(f'Scatter Plot: {x_metric} vs {y_metric}', fontsize=16)
    plt.xlabel(x_metric, fontsize=14)
    plt.ylabel(y_metric, fontsize=14)
    
    # Save the plot as an image
    plt.savefig(f'scatter_{x_metric}_vs_{y_metric}.png')
    plt.show()

# Example: Create scatter plot of 'Attendance (%)' vs 'Avg Exam Score (%)'
create_scatter_plot('Attendance (%)', 'Avg Exam Score (%)')

# Example: Create scatter plot of 'Understanding Level (1-5)' vs 'Engagement Level (1-5)'
create_scatter_plot('Understanding Level (1-5)', 'Engagement Level (1-5)')

print("Scatter plots created successfully")

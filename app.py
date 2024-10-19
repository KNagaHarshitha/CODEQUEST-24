from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scatter_plot', methods=['POST'])
def scatter_plot_view():
    # Retrieve the user inputs from the form
    attendance = [int(x) for x in request.form['attendance'].split(',')]
    understanding = [int(x) for x in request.form['understanding'].split(',')]
    engagement = [int(x) for x in request.form['engagement'].split(',')]
    learning_env = [int(x) for x in request.form['learning_env'].split(',')]
    peer_influence = [int(x) for x in request.form['peer_influence'].split(',')]

    # Prepare data for the scatter plot
    user_data = {
        'attendance': attendance,
        'understanding': understanding,
        'engagement': engagement,
        'learning_env': learning_env,
        'peer_influence': peer_influence
    }

    # Plot the scatter plot using the new function
    img = io.BytesIO()  # Create a buffer to hold the image
    plot_scatter_plot(user_data)  # Call the plotting function
    plt.savefig(img, format='png')  # Save the plot to the buffer
    img.seek(0)  # Reset buffer position

    # Encode the image to display it in the browser
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()  # Close the plot

    return render_template('index.html', graph_url='data:image/png;base64,{}'.format(graph_url))

def plot_scatter_plot(data):
    # Unpacking the data dictionary for ease of access
    attendance = data['attendance']
    understanding = data['understanding']
    engagement = data['engagement']
    learning_env = data['learning_env']
    peer_influence = data['peer_influence']

    # Number of observations
    observations = list(range(1, len(attendance) + 1))

    # Creating the scatter plot
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plotting the attendance (separate scale)
    ax1.scatter(observations, attendance, label='attendance', color='blue', marker='o')
    ax1.set_xlabel('Observations')
    ax1.set_ylabel('Attendance (%)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Creating a secondary axis for the other metrics
    ax2 = ax1.twinx()
    ax2.scatter(observations, understanding, label='understanding', color='orange', marker='o')
    ax2.scatter(observations, engagement, label='engagement', color='green', marker='o')
    ax2.scatter(observations, learning_env, label='learning_env', color='red', marker='o')
    ax2.scatter(observations, peer_influence, label='peer_influence', color='purple', marker='o')
    ax2.set_ylabel('Other Metrics (1-5)', color='black')

    # Adding titles and legend
    fig.suptitle('Scatter Plot of Student Metrics', fontsize=14)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Show grid and plot
    ax1.grid(True)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)

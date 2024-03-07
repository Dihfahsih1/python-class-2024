from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io

app = Flask(__name__)

# Load data from CSV
data = pd.read_csv('csv_file.csv')

@app.route('/')
def index():
    # Plot graph
    plt.figure(figsize=(10, 6))
    plt.plot(data['Index'], data['Number of employees'], marker='o')
    plt.title('Number of Employees by Index')
    plt.xlabel('Index')
    plt.ylabel('Number of Employees')

    # Convert plot to base64 string
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Render template with plot
    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)

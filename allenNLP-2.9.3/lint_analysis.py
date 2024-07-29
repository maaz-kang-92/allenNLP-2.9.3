import pandas as pd
import matplotlib.pyplot as plt

def plot_chart(csv_file):
    df = pd.read_csv(csv_file)

    # Assuming your CSV has columns named 'Category' and 'Count'
    categories = df['Category']
    counts = df['Count']

    plt.bar(categories, counts, color='blue')
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.title('CSV Data Visualization')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

if __name__ == "__main__":
    csv_file_path = r'G:\books\7th semester\FYP\1st\sonar-scanner-5.0.1.3006-windows\bin\AllenNLP\allennlp-2.9.3\allennlp\your_csv_file.csv'
    plot_chart(csv_file_path)

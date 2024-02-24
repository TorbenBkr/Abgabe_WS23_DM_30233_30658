import os
import random
import csv

# Specify the path to the input CSV file
input_file = './tripadvisor_review.csv'

# Specify the path to the output CSV file
output_file = './output.csv'

# Read the input CSV file
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Remove the first column from the data
data = [row[1:] for row in data]

# Keep the first row in the data
header = data[0]

# Filter out duplicates from the data
input_file = list(set(tuple(row) for row in input_file))

# Calculate the number of rows to keep (90% of the total rows)
num_rows = int(len(data) * 0.9)

# Select random num_rows rows from the data
selected_data = random.sample(data[1:], num_rows)

# Add the header back to the selected data
selected_data.insert(0, header)

# Write the selected data to the output CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(selected_data)


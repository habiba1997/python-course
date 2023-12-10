import json
import csv


def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header
        header = data[0].keys() if isinstance(data, list) and len(data) > 0 else data.keys()
        csv_writer.writerow(header)

        # Write the data
        if isinstance(data, list):
            for row in data:
                csv_writer.writerow(row.values())
        elif isinstance(data, dict):
            csv_writer.writerow(data.values())
        else:
            raise ValueError("Invalid JSON format")

    print(f"Conversion completed. CSV file saved to {csv_file_path}")


# Example usageC:\Users\habiba.ahmed\Downloads\overtime data\ProductionOrderBatch30.json
json_file_path = "C:/Users/habiba.ahmed/Downloads/overtime data/ProductionOrderBatch30.json"
csv_file_path = "C:/Users/habiba.ahmed/Downloads/overtime data/example.csv"
json_to_csv(json_file_path, csv_file_path)

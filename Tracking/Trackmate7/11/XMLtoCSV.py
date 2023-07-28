import os
import csv
import xml.etree.ElementTree as ET

def xml_to_csv(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Get the folder path of the XML file
    folder_path = os.path.dirname(xml_file)

    # Construct the CSV file path
    csv_file = os.path.join(folder_path, "output.csv")

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        headers = []
        rows = []

        for element in root.iter():
            if element.tag not in headers:
                headers.append(element.tag)

        writer.writerow(headers)

        for child in root:
            row = []
            for header in headers:
                data = child.find(header)
                if data is not None:
                    row.append(data.text)
                else:
                    row.append('')
            rows.append(row)

        writer.writerows(rows)

    print(f"Conversion complete. CSV file '{csv_file}' has been created.")

# Usage example
xml_file_path = '/Users/lian/Desktop/Tracking/Trackmate7/11/_Tracks.xml'
xml_to_csv(xml_file_path)
 
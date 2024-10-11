import json
import pandas as pd
import os

# Load JSON data
file_path = 'regencies.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Creating a mapping for province names and their IDs
province_mapping = {
    "Jawa Barat": "32",
    "DKI Jakarta + Kep Seribu": "31",
    "Banten": "36",
    "Jawa Tengah": "33",
    "DI Yogyakarta": "34",
    "Jawa Timur": "35"
}

provinces_data = {province: [] for province in province_mapping.keys()}

for entry in data:
    province_id = entry['province_id']
    for province_name, pid in province_mapping.items():
        if province_id == pid:
            provinces_data[province_name].append({
                "id": entry["id"],
                "province_id": entry["province_id"],
                "name": entry["name"],
                "alt_name": entry["alt_name"],
                "latitude": entry["latitude"],
                "longitude": entry["longitude"],
            })

output_dir = 'provinces_csv'
os.makedirs(output_dir, exist_ok=True)

for province, entries in provinces_data.items():
    if entries:  # Only create CSV if there are entries
        df = pd.DataFrame(entries)
        output_path = os.path.join(output_dir, f'{province}.csv')
        df.to_csv(output_path, index=False)

print(f"CSV files created in the '{output_dir}' directory.")

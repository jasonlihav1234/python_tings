### reading csv files with csv.reader
# iterate over rows, returning each as a list of strings
# use next(reader) to skip or extract the header
# accepts delimiter, quotechar, and other formatting parameters

import csv
from pathlib import Path

csv_path = Path("servers.csv")

with csv_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"Header: {header}")

    for idx, row in enumerate(reader, start=1):
        print(f"Row {idx}: {row}")

### csv.DictReader -> reads rows into dictionary
csv_path = Path("servers.csv")

with csv_path.open("r", encoding="utf-8", newline="") as file:
    dict_reader = csv.DictReader(file)
    print(f"Fieldnames: {dict_reader.fieldnames}")

    for idx, record in enumerate(dict_reader, start=1):
        print(f"Record {idx}: {record}")


### csv.writer -> write rows from lists using .writenow() or .writerows()
# open file with newline='' to avoid blank lines
data = [
    ["hostname", "ip-address", "role"],
    ["web02", "10.0.1.6", "webserver"]
]

out_path = Path("output_basic.csv")

with out_path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


### csv.DictWriter
records = [
    {
        "host": "web01",
        "port": "80",
        "status": "running"
    },
    {
        "host": "db02",
        "port": "5432",
        "status": "maintenance"
    }
]

fieldnames = set()
for record in records:
    fieldnames = fieldnames | record.keys()

out_dict_path = Path("output_dict.csv")

with out_dict_path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, restval="undefined", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(records)

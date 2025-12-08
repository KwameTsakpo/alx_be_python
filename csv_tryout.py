import csv

def instantiate_csv():
    rows = []

    # Step 1: Read the CSV into a list of dictionaries
    with open('items.csv', 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames  # Save headers
        for row in reader:
            # Modify Sylvia's age
            if row['name'] == 'Sylvia':
                row['age'] = '25'
            rows.append(row)
            print(rows)

    # Step 2: Overwrite the entire CSV with updated data
    with open('items.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()      # Write column names
        writer.writerows(rows)    # Write all updated rows
    
    print(rows)

instantiate_csv()

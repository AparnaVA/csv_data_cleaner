
import csv

# Function to clean customer data
def clean_csv_file():

    # Get input file from user
    input_file = input("Enter the CSV file path: ")

    # Ask the user which columns are mandatory
    mandatory_input = input(
        "Enter mandatory columns separated by commas (e.g., Name,Email): "
    )

    mandatory_columns = mandatory_input.split(",")

    # Remove spaces from mandatory column names
    mandatory_columns = [column.strip() for column in mandatory_columns]

    # Lists to store records
    cleaned_records = []
    invalid_records = []
    seen_records = []

    total_records = 0
    duplicates_removed = 0

    # Read the CSV file
    try:
        with open(input_file, "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            # Check whether mandatory columns exist in the CSV
            for column in mandatory_columns:
                if column not in reader.fieldnames:
                    print("Error: Column", column, "does not exist.")
                    return

            # Process each row
            for row in reader:

                total_records += 1

                # Remove unnecessary spaces from all fields
                for key in row:
                    if row[key] is not None:
                        row[key] = row[key].strip()

                # Check for missing mandatory fields
                missing_fields = []

                for column in mandatory_columns:
                    if not row[column]:
                        missing_fields.append(column)

                if missing_fields:
                    reason = "Missing mandatory fields: " + ", ".join(missing_fields)

                    invalid_records.append({
                        "Name": row.get("Name", ""),
                        "Email": row.get("Email", ""),
                        "Phone": row.get("Phone", ""),
                        "City": row.get("City", ""),
                        "Reason": reason
                    })

                    continue

                # Validate email
                email = row.get("Email", "")

                if "@" not in email or "." not in email.split("@")[-1]:
                    invalid_records.append({
                        "Name": row.get("Name", ""),
                        "Email": email,
                        "Phone": row.get("Phone", ""),
                        "City": row.get("City", ""),
                        "Reason": "Invalid email format"
                    })

                    continue

                # Standardize city capitalization
                if row.get("City"):
                    row["City"] = row["City"].title()

                # Check duplicate records
                if row in seen_records:
                    duplicates_removed += 1
                    continue

                seen_records.append(row.copy())

                # Add valid record
                cleaned_records.append(row)

        # Write cleaned records to CSV
        if cleaned_records:
            with open("cleaned_customers.csv", "w", newline="", encoding="utf-8") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=reader.fieldnames
                )

                writer.writeheader()
                writer.writerows(cleaned_records)

        # Write invalid records to CSV
        with open("invalid_records.csv", "w", newline="", encoding="utf-8") as file:

            fieldnames = ["Name", "Email", "Phone", "City", "Reason"]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(invalid_records)

        # Display summary
        print("\n--- Cleaning Summary ---")
        print("Total records processed:", total_records)
        print("Duplicates removed:", duplicates_removed)
        print("Valid records:", len(cleaned_records))
        print("Invalid records:", len(invalid_records))
        print("\nFiles generated successfully.")

    except FileNotFoundError:
        print("Error: CSV file not found.")

    except Exception as error:
        print("Something went wrong:", error)


# Call the function
clean_csv_file()

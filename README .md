# CSV Customer Data Cleaning using Python

## Project Description

This is a beginner-friendly Python project that cleans customer data stored in a CSV file.

Customer data may contain duplicate records, missing values, inconsistent formatting, unnecessary spaces, and invalid email addresses. This program helps clean the data automatically and generates separate files for valid and invalid records.

## Features

- Reads customer data from a CSV file.
- Removes duplicate records.
- Identifies missing mandatory fields.
- Standardizes city names using consistent capitalization.
- Removes unnecessary spaces from text fields.
- Validates email addresses using basic formatting rules.
- Generates a cleaned CSV file containing valid records.
- Generates a separate CSV report containing invalid records and the reasons they were rejected.
- Allows users to specify which columns are mandatory.
- Displays a summary of the data cleaning process.

## Technologies Used

- Python
- CSV module
- File Handling
- Lists and Dictionaries
- Functions
- Loops and Conditional Statements

## Project Structure

```text
CSV_Cleaning_Project/
│
├── csv_cleaner.py
├── customers.csv
├── cleaned_customers.csv
├── invalid_records.csv
└── README.md
```

- `csv_cleaner.py` – Main Python program.
- `customers.csv` – Input file containing customer data.
- `cleaned_customers.csv` – Output file containing cleaned and valid records.
- `invalid_records.csv` – Output file containing invalid records and their reasons.
- `README.md` – Project documentation.

## Sample Input

The input CSV file should contain customer details with the following columns:

```csv
Name,Email,Phone,City
John,john@gmail.com,9876543210,Kochi
Mary,mary@gmail.com,,Trivandrum
John,john@gmail.com,9876543210,Kochi
Alex,alex@gmail.com,9876543211,kochi
,unknown@gmail.com,9876543212,Kozhikode
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project folder

```bash
cd CSV_Cleaning_Project
```

### 3. Run the Python program

```bash
python csv_cleaner.py
```

### 4. Enter the input CSV file path

```text
Enter the CSV file path: customers.csv
```

### 5. Specify the mandatory columns

Enter the columns that must contain values, separated by commas.

```text
Enter mandatory columns separated by commas (e.g., Name,Email): Name,Email,Phone
```

The program will process the file and generate the output CSV files.

## Sample Output

### cleaned_customers.csv

Contains valid records after removing duplicates, cleaning spaces, and standardizing city names.

```csv
Name,Email,Phone,City
John,john@gmail.com,9876543210,Kochi
Alex,alex@gmail.com,9876543211,Kochi
```

### invalid_records.csv

Contains records that could not be processed, along with the reason.

```csv
Name,Email,Phone,City,Reason
Mary,mary@gmail.com,,Trivandrum,Missing mandatory fields: Phone
,unknown@gmail.com,9876543212,Kozhikode,Missing mandatory fields: Name
```

## Summary Report

After processing, the program displays:

- Total records processed
- Number of duplicates removed
- Number of valid records
- Number of invalid records
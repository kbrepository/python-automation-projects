import csv
import json
import os
from collections import defaultdict

EXPENSE_FILE = 'expenses.csv'

def add_expense(date, category, amount, note):
    file_exists = os.path.isfile(EXPENSE_FILE)
    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Date', 'Category', 'Amount', 'Note'])
        writer.writerow([date, category, amount, note])
    print(f"✅ Added: {category} - ₹{amount} on {date}")

def show_summary():
    summary = defaultdict(float)
    try:
        with open(EXPENSE_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                summary[row['Category']] += float(row['Amount'])
    except FileNotFoundError:
        print("No expenses found.")
        return

    print("\n📊 Expense Summary:")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")

def export_to_json():
    data = []
    try:
        with open(EXPENSE_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)

        with open('expenses.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("✅ Exported data to expenses.json")
    except FileNotFoundError:
        print("No expenses to export.")

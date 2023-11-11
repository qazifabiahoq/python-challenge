import csv
import os
import sys

csv_path = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

total_months = 0
net_total = 0
monthly_changes = []
previous_profit_loss = None
# These are the Variables to keep track of the greatest increase and decrease
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

with open(csv_path, 'r') as file:
    csvreader = csv.reader(file)
    
  
    header = next(csvreader)
        # Removed the line that skips the header, so the header will be included in processing
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        total_months += 1
        net_total += profit_loss
        # Calculating and appending the monthly change
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            monthly_changes.append(change)
      # Updating the greatest increase and decrease if applicable
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date
# Updating the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

average_change = sum(monthly_changes) / len(monthly_changes)
# This is the file path for the output text file
output_file_path = os.path.join(os.path.dirname(__file__), "Analysis", "financial_analysis.txt")

with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")


sys.stdout.write("Financial Analysis\n")
sys.stdout.write("----------------------------\n")
sys.stdout.write(f"Total Months: {total_months}\n")
sys.stdout.write(f"Total: ${net_total}\n")
sys.stdout.write(f"Average Change: ${average_change:.2f}\n")
sys.stdout.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
sys.stdout.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

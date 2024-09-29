import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank/Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank/Resources/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
net_total = 0
net_change_list = []
previous_profit_loss = None
greatest_increase = ("", 0)  # (month, amount)
greatest_decrease = ("", 0)  # (month, amount)

# Open and read the csv
with open(file_to_load, 'r') as financial_data:
    fin_reader = csv.reader(financial_data)
    # Skip the header row
    header = next(fin_reader)
    
    # Process each row of data
    for row in fin_reader:
        month = row[0]
        profit_loss = float(row[1])
        
        # Track the total
        total_months += 1
        net_total += profit_loss
        
        # Calculate the change in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            net_change_list.append(change)
            
            # Check for greatest increase
            if change > greatest_increase[1]:
                greatest_increase = (month, change)
            
            # Check for greatest decrease
            if change < greatest_decrease[1]:
                greatest_decrease = (month, change)
        
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

# Print results
print(f"Total Months: {total_months}")
print(f"Net Total Profit/Loss: ${int(net_total)}")  # Convert to whole number
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${int(greatest_increase[1])})")  # Convert to whole number
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${int(greatest_decrease[1])})")  # Convert to whole number
# Export the results to a text file
with open(file_to_output, 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Net Total Profit/Loss: ${int(net_total)}\n")  # Convert to whole number
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${int(greatest_increase[1])})\n")  # Convert to whole number
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${int(greatest_decrease[1])})\n")  # Convert to whole number
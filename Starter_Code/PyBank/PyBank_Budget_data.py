import csv
import os
from datetime import datetime



file_path = "./Resources/budget_data.csv"
print(file_path)

#code explained by tutor for file_path

if file_path is None:
    print("Error")
else:
    # Opening and reading data from csv file
    with open(file_path, newline='') as budget_data:
        reader = csv.reader(budget_data)

        header = next(reader)

        # Initiating Variables
        total_months = 0
        net_total = 0
        previous_profit_loss = None
        changes_in_profit_loss = []
        greatest_increase = {"date": None, "amount": float("-inf")}
        greatest_decrease = {"date": None, "amount": float("inf")}

        # Loop through each row in the CSV
        for row in reader:
            # Extracting data
            date = datetime.strptime(row[0], "%b-%y")
            profit_loss = int(row[1])
            
            # Calculate total months and net total
            total_months += 1 
            net_total += int(row[1])
            
            # Calculate changes in profit/loss
            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss
                changes_in_profit_loss.append(change)
                
                # Update greatest increase and decrease
                if change > greatest_increase["amount"]:
                    greatest_increase["date"] = date
                    greatest_increase["amount"] = change
                if change < greatest_decrease["amount"]:
                    greatest_decrease["date"] = date
                    greatest_decrease["amount"] = change
            
            # Update previous profit/loss for the next iteration
            previous_profit_loss = profit_loss

        # Calculate average change
        if len(changes_in_profit_loss) > 0:
            average_change = sum(changes_in_profit_loss) / len(changes_in_profit_loss)
        else:
            average_change = 0

         
        #print analysis result
        analysis_result = f"Financial Analysis\n----------------------------\n"
        analysis_result += f"Total Months: {total_months}\n"
        analysis_result += f"Total: ${net_total}\n"
        analysis_result += f"Average Change: ${average_change:.2f}\n"
        analysis_result += f"Greatest Increase in Profits: {greatest_increase['date'].strftime('%b-%y')} (${greatest_increase['amount']})\n"
        analysis_result += f"Greatest Decrease in Profits: {greatest_decrease['date'].strftime('%b-%y')} (${greatest_decrease['amount']})\n"

        # Create the 'analysis' folder if it doesn't exist
        if not os.path.exists('analysis'):
            os.makedirs('analysis')

        # Open a new file in the 'analysis' folder and write the analysis result
        with open('analysis/analysis_result.txt', 'w') as file:
            file.write(analysis_result)

        # Print analysis results
        print(analysis_result)
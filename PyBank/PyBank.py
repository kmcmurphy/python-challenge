import os
import csv

# Open the data
csvpath = os.path.join('Resources','budget_data.csv')

# Get some empty lists set up
date = []
month = []
year = []
profit_loss = []
profit_difference = []
count = 0

# Loop through the data
with open(csvpath, encoding="utf8") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        csvheader = next(csvreader)
        #print(f"CSV Header: {csvheader}")

        for row in csvreader:
            # Add the date
            date.append(row[0])
            
            split_date = row[0].split("-")
            month.append(split_date[0])
            year.append(split_date[1])

            profit_loss.append(int(row[1]))

            # Normalize numbers to get a total and then +/- based on monthly rise or fall
            current_profit = profit_loss[count]
            last_profit = profit_loss[count - 1]

            if current_profit >= last_profit:
                difference = current_profit - last_profit
               
            else: 
                difference = (last_profit - current_profit) * -1

            profit_difference.append(difference)

            count = count + 1

        #Set variables for the min/max difference and dates they align with
        max_value = (max(profit_difference))
        max_index = profit_difference.index(max_value)

        min_value = min(profit_difference)
        min_index = profit_difference.index(min_value)

        average_change = float(sum(profit_difference)/(len(month)-1))

        #print output
        output_lines = [
        "Financial Analysis",
        "----------------------------",
        f"Total Months: {len(month)}",
        f"Total: ${sum(profit_loss)}",
        f"Average Change: ${round(average_change,2)}",
        f"Greatest Increase in Profits: {date[max_index]} (${max_value})",
        f"Greatest Decrease in Profits: {date[min_index]} (${min_value})"
        ]

# Specify the file to write to
output_path = os.path.join("Output", "new.txt")

# Open a file using "write" mode and create a variable to hold output
with open(output_path, 'w') as txtfile:

    # Take each line/item from list and add a line break
    txtfile.write('\n'.join(output_lines))
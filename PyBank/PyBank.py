import os
import csv


#NEED TO INVESTIGATE - BE SURE YOU'RE IN THE RIGHT TERMINAL DIRECTORY TO RUN
csvpath = os.path.join('Resources','budget_data.csv')

date = []
month = []
year = []
profit_loss = []
profit_difference = []
count = 0

with open(csvpath, encoding="utf8") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        csvheader = next(csvreader)
        print(f"CSV Header: {csvheader}")

        for row in csvreader:
            # Add the date
            date.append(row[0])
            
            split_date = row[0].split("-")
            month.append(split_date[0])
            year.append(split_date[1])

            prior_profit = 0

            profit_loss.append(int(row[1]))
            #monthlyprofit = ((profit_loss[count]))-(profit_loss[count-1])
            #profit_difference.append(monthlyprofit)

            # Normalize numbers to get a total and then +/- based on monthly rise or fall
            current_profit = profit_loss[count]
            last_profit = profit_loss[count - 1]

            #make both profits positive
            if current_profit < 0:
                current_profit_pos = current_profit * -1 
            else:
                current_profit_pos = current_profit

            if last_profit < 0:
                last_profit_pos = last_profit * -1
            else:
                 last_profit_pos = last_profit

            profit_spread = last_profit_pos + current_profit_pos

            if current_profit < 0:
                profit_spread =  profit_spread * -1
            # if current month is negative, make positive and then times -1 to make loss 

            # if current_profit > 0 and last_profit > 0:
            #     #sub abs
            #     profit_spread = abs(current_profit) - abs(last_profit)
            #     profit_spread = profit_spread * -1
            
            # elif current_profit < 0 and last_profit < 0:
            #     #sub abs
            #     profit_spread = abs(current_profit) - abs(last_profit)
            #     profit_spread = profit_spread * -1

            # elif current_profit < 0 or last_profit < 0:
            #     #add abs
            #     profit_spread = abs(current_profit) + abs(last_profit)
            #     #profit_spread = profit_spread * -1

            profit_difference.append(profit_spread)
            print(profit_spread, date[count])


            count = count + 1


        print (sum(profit_loss))
        print (sum(profit_loss)/len(profit_loss))
        print(len(month))
        print(max(profit_difference))
        print(min(profit_difference))

        # title = "Alien"

        # for row in csvreader:
        #     print(row[0])
        #     row_title = row[0]
        #    #if row_title == title:
        #     #    print(f"{title} was publised by")
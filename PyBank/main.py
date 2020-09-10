import os
import csv

budget_data = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    Profit = []
    months = []

    for rows in csv_reader:
        Profit.append(int(rows[1]))
        months.append(rows[0])

    
    revenue_change = []

    for x in range(1, len(Profit)):
        revenue_change.append((int(Profit[x]) - int(Profit[x-1])))
    
    revenue_average = sum(revenue_change) / len(revenue_change)

    months_total = len(months)

    greatest_increase = max(revenue_change)

    greatest_decrease = min(revenue_change)


 #-------------------------------------------------------------------------
    print("Financial Analysis")

    print("........................................................")

    print("total months: " + str(months_total))

    print("Total: " + "$" + str(sum(Profit)))

    print("Average change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))




    file = open("PyBank_Summary.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("......................................................." + "\n")

    file.write("total months: " + str(months_total) + "\n")

    file.write("Total: " + "$" + str(sum(Profit)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()

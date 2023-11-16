#!/usr/bin/env python
# coding: utf-8

# In[27]:


#importing modules
import csv
import os

#defining file paths for files going to be used to load and output
file_to_load = os.path.join(".", "Resources", "budget_data.csv")
file_to_output = os.path.join(".", "budget_analysis.txt")

#defining total months to later calculate the total number of months
total_months = 0

#defining the total net to later calculate P&L over the entire period
total_net = 0

#creating a net change list to track changes
net_change_list = []
month_of_changes = []

#found this method to calculate greatest increase and decrease via Bing AI help
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]

#reading the .csv file and converting it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    #exporting data without header from the file
    header = next(reader)
    first_row = next(reader)
    
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
#calculating the total number of months in the dataset
    total_months += 1
    
    for row in reader:
    
#calculating the P&L over the entire period
        total_net += int(row[1])
    
#tracking the total & net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        
#calculating the greatest increase
        if(net_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
            
#calculating the greatest decrease
        if(net_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#defining the monthly average
net_monthly_average = sum(net_change_list)/len(net_change_list)
    
output = (f"Financial Analysis\n"
          f"-----------------------------\n"
          f"Total Months: {total_months}\n"
          f"Total: ${total_net}\n"
          f"Average Change: ${net_monthly_average}\n"
          f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
          f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
        
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


# In[ ]:





# In[ ]:





# In[ ]:





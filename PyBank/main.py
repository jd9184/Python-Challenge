import csv

file_to_load = "Resources/budget_data.csv"
file_to_output = "Analysis/budget_analysis.txt"

#track revenue parameters
total_months = 0
prev_revenue = 0
month_of_change = 0
revenue_change = 0
total_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",9999999999999999999]
total_revenue = 0

#read csv and convert into list of dictionaries
with open(file_to_load) as revenue_data:
	reader = csv.reader(revenue_data)
	next(reader)

	for row in reader:
		# track the totals
		total_months = total_months + 1
		total_revenue = total_revenue + int(row[1])

		#track revenue change
		if prev_revenue !=0:
			revenue_change = int(row[1]) - prev_revenue
			total_change = total_change + revenue_change  
			month_of_change = month_of_change + 1
		
		
		prev_revenue = int(row[1])
	


		#calculate the greatest increase
		if (revenue_change > greatest_increase[1]):
			greatest_increase[0] = row[0]
			greatest_increase[1] = revenue_change

					#calculate the greatest decrease
		if (revenue_change < greatest_decrease[1]):
			greatest_decrease[0] = row[0]
			greatest_decrease[1] = revenue_change 

#calculate the average revenue change    
average_change = total_change / month_of_change
print(month_of_change)

# print(len(revenue_change_list))

 #generate out put summary
output = (
	f"\nFinancial Analysis\n"
	f"--------------------------\n"
	f"Total Months: {total_months}\n"
	f"Total Revenue: ${total_revenue}\n"
	f"Average Revenue Change: ${average_change:.2f}\n"
	f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
	f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n"

)

# print(revenue_change_list)
#print (sum(revenue_change_list))

#print the output
print(output)

with open(file_to_output, "w") as outfile:
	outfile.write(output)




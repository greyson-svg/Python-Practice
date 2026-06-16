#Lists - Exercise
#Selling lemonade

#- You sell lemonade over two weeks, the lists show number of lemonades sold per week
#- Profit for each lemonde sold is 1.5$
#. Add another day to week 2 list by capturing a number as input
#. Combine the two lists into the list called 'sales'
#. Calculate/ print how much you have earned on
#· Best day
#· Worst day
#Separately and in total

#2 Separate weeks of sales in 2 lists. 
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]

#collects user input for the added sales in the second week
#adds the 2 weeks into one list without modifying the original lists.
extra_sale = int(input('What amount do you want to add in for week 2 sales?'))
sales_w2.append(extra_sale)
sales = sales_w1 + sales_w2


#prints the lowest, highest, and total sales, after calculating each. 
print(f'The lowest recorded sales were {min(sales) * 1.5}')
print(f' The highest recorded sales was {max(sales) * 1.5}')
print(f' The total recorded sales was {(min(sales) + max(sales)) * 1.5}')
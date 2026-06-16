
# 🏁 Pit Stop Timing Optimizer 🔧

#

# 1. Ask the user for the total race time in seconds.

# 2. Ask how many pit stops were made.

# 3. Ask for the average pit stop duration (in seconds).

#

# Then:

# - Calculate the total pit stop time.

# - Calculate the percentage of the race spent in the pits.

# - Round the percentage to 2 decimal places.

#

# Finally, print all of the following:

# - Total pit stop time in seconds

# - Percentage of race time spent in pits

# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

#collects inputs for racing times

total_race_time = input('What was the total race time?')
total_pit_stops = input('How many pit stops were made in total?')
average_pit_stop_duration = input('What was the average pit stop duration in seconds?')



#calculates averages, time spent in race pit, and rounds that value to 2 dec places

total_time_at_pit_stop = float(average_pit_stop_duration) * int(total_pit_stops)
percentage_of_race_time_in_pits = float((total_time_at_pit_stop) / float(total_race_time)) * 100
rounded_value = round(percentage_of_race_time_in_pits, 2)



#Prints the results

print(f' Your teams total time spent in the pits is {total_time_at_pit_stop}!')
print(f' Your total percentage of race time spent in the pits was {rounded_value} percent!')



if percentage_of_race_time_in_pits > 5:
    print('You need a new pit crew.🛠️')
else:
     print('Your team is doing great, but get faster!')

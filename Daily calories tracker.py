# Daily Calorie Tracker
import datetime
print("Daily Calorie Tracker")
print("---------")

# Enter daily calories limit
calorie_limit = float(input("Enter your daily calorie limit: "))

# Enter number of meals
num_meals = int(input("How many meals did you have today? "))

meals = []
calories = []

#Enter meal info.
for i in range(num_meals):
    print("\nMeal", i + 1)
    meal_name = input("Enter meal name: ")
    meal_calories = float(input("Enter calories: "))
    meals.append(meal_name)
    calories.append(meal_calories)

# Calculate total and average of total calories intake
total = sum(calories)
average = total / num_meals

if total > calorie_limit:
    print("\nYou have exceeded your daily limit by", total - calorie_limit, "calories.")
else:
    print("\nYou are within your daily calorie limit!")

# tell the daily report
print("\n--- Daily Report ---")
for i in range(num_meals):
    print(meals[i], ":", calories[i], "calories")

print("Total calories:", total)
print("Average calories per meal:", average)

# Option to save the report or not 
save = input("\nDo you want to save this report? (yes/no): ")

if save.lower() == "yes":
    file = open("calorie_log.txt", "w")
    file.write("Daily Calorie Tracker Log\n")
    file.write("Date: " + str(datetime.datetime.now()) + "\n\n")
    for i in range(num_meals):
        file.write(meals[i] + " : " + str(calories[i]) + " calories\n")
    file.write("\nTotal: " + str(total) + "\n")
    file.write("Average: " + str(average) + "\n")
    if total > calorie_limit:
        file.write("Status: Exceeded limit\n")
    else:
        file.write("Status: Within limit\n")
    file.close()
    print("Report saved as calorie_log.txt")
else:
    print("Report not saved.")

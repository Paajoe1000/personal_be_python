# prompt for a single Task
task = input("Enter your task: ").lower
priority = input("Priority (high/medium/low): ").lower
time_bound = input("Is it time-bound? (yes/no): ").lower

# Initializing the reminder message
if time_bound == "yes":
    reminder = f"Reminder: '{task}' is a "
else: 
    reminder = f"Note: '{task}' is a "

# Process the task based on priority and time sensitvity
match priority:
    case "high":
        reminder += f"'{task}' is a high priority task."
    case "medium":
        reminder += f"'{task}' is a medium priority task."
    case "low":
        reminder += f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority level."
        

# Determine if the task is time-bound and modify the reminder
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += "consider completing it when you have free time."
    
    print(f"Reminder: {reminder} that requires immediate attention today!")

    print(f"Note: {reminder}. Consider completing it when you have free time.")
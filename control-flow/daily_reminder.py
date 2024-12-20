# Prompt the user to input the task, priority level, and if the task is time-bound.
task = input("Describe the task you would like to do today:")
priority = input("Enter the priority level (high, medium, low):").strip().lower()
time_bound = input("Is the task time-bound? (yes/no):").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: High priority task - {task}. Time-bound task.")
        else:
            print(f"Reminder: High priority task - {task}. Not time-bound.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: Medium priority task - {task}. Time-bound task.")
        else:
            print(f"Reminder: Medium priority task - {task}. Not time-bound.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: Low priority task - {task}. Time-bound task.")
        else:
            print(f"Reminder: Low priority task - {task}. Not time-bound.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
    


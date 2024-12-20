# Prompt the user to input the task, priority level, and if the task is time-bound.
Task = input("Describe the task you would like to do today:")
Priority = input("Enter the priority level (high, medium, low):").strip().lower()
Time_Bound = input("Is the task time-bound? (yes/no):").strip().lower()

match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"Reminder: High priority task - {Task}. Time-bound task.")
        else:
            print(f"Reminder: High priority task - {Task}. Not time-bound.")
    case "medium":
        if Time_Bound == "yes":
            print(f"Reminder: Medium priority task - {Task}. Time-bound task.")
        else:
            print(f"Reminder: Medium priority task - {Task}. Not time-bound.")
    case "low":
        if Time_Bound == "yes":
            print(f"Reminder: Low priority task - {Task}. Time-bound task.")
        else:
            print(f"Reminder: Low priority task - {Task}. Not time-bound.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
    


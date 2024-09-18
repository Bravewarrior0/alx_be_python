task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

msg = ""
match priority:
    case "high":
        msg = "Consider completing it as soon as possible."
    case "medium":
        msg = "Consider completing it after the high priority tasks"
    case "low":
        msg = "Consider completing it when you have free time."

if msg != "":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority} task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a {priority} task. {msg}")

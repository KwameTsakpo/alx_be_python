task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

def print_reminder():
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has an unknown priority level"

    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        if priority in ["high", "medium"]:
            message += ". Try to complete it soon."
        else:
            message += ". Consider completing it when you have free time."

    print("\nReminder:", message)


while True:
    print_reminder()
    answer = input("\nIs this reminder okay? (yes/no): ").lower()
    if answer == "yes":
        print("Great! Good luck with your task!")
        break
    else:
        task = input("Enter your task: ")
        priority = input("Priority (high/medium/low): ").lower()
        time_bound = input("Is it time-bound? (yes/no): ").lower()

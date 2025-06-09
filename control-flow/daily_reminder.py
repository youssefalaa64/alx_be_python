task = input("Enter your task:")
priority = input("Priority (high, medium, low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority :
    case "high" :
        print("Reminder:'Finish project report' is a high priority task that requires immediate attention today!  ")
    case "low" :
        print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case "medium" :
        print("Reminder: finish this after finishing your high priority task first")
if time_bound == "yes" :
    print("Reminder:'Finish project report' is a high priority task that requires immediate attention today! ")
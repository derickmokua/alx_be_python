#!/usr/bin/env python3
# Daily Reminder Program
# This program provides customized task reminders based on priority and time sensitivity

# Prompt for task input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    # Different messages based on priority for non-time-bound tasks
    match priority:
        case "high":
            print(f"Note: {reminder}. Try to complete it as soon as possible.")
        case "medium":
            print(f"Note: {reminder}. Consider completing it when you have time.")
        case "low":
            print(f"Note: {reminder}. Consider completing it when you have free time.")
        case _:
            print(f"Note: {reminder}. Please set a proper priority level.")

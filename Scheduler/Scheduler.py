import module as m
import datetime
import csv
import os


continues = True
while continues:
    # Load csv
    # reasoning: loads every time the csv is updated/modified
    if os.path.isfile('schedule.csv'):
        with open('schedule.csv', 'r') as data:
            dictionaries = csv.DictReader(data)
            entire_schedule = list(dictionaries)

    val = input("__________________________________________________________\nSelect one of the following main menu option: \n [C]reate, [V]iew schedules, [D]elete Event, [Q]uit\n")
    val = val.upper()

    if val == 'Q':
        continues = False
        print("Quitting...\n")

    elif val == 'C':
        name = m.request_name(entire_schedule)
        startTime, endTime = m.compare_time()
        date = m.request_date()
        #repeat = input("Would you like to repeat this event [N]one, [D]aily, [W]eekly:\n")
        if (m.compare_datetime(entire_schedule, date, startTime, endTime)):
            m.create(name, startTime, endTime, date)
            print("Successfully Created an Event\n")
        else:
            print("Invalid event: Time conflict(s) between events\n")
            continue
        
    elif val == "D":
        name = m.request_name(entire_schedule, True)
        print("Deleting")

    elif val == "V":
        print('\nschedule: \n', entire_schedule, '\n')

    else:
        print("Error: Incorrect Input Format\n")

print("done")
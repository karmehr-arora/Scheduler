import datetime
import csv
import os

def create(Name, startTime, EndTime, Date):
    mydict = [{'date': Date.strftime("%m-%d-%Y"), 'start': startTime.strftime("%H:%M"), 'end': EndTime.strftime("%H:%M"), 'name': Name}]
    field = ['date', 'start', 'end', 'name']

    if os.path.isfile('schedule.csv'):
        with open('schedule.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = field)
            writer.writerows(mydict)
    else:
        with open('schedule.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = field)
            writer.writeheader()
            writer.writerows(mydict)

def request_name(entire_schedule):
    res = [ history['name'] for history in entire_schedule]
    name_unique = False
    while not name_unique:
        name = input("Name of Event:\n")
        checked = False
        for hist in res:
            if(name.lower() == hist.lower()):
                checked = True
        if (checked):
            print("Name is already in use. Please enter a valid name.\n")
        else:
            name_unique = True

    return name


def request_time(start_end):
    prompt = start_end + " Time: (24 hr format)\n"
    time_correct = False
    while not time_correct:
        try:
            time = input(prompt)
            time = datetime.datetime.strptime(time, "%H:%M")
            time_correct = True
        except:
            print ("Please enter correct time in HH:MM format\n")

    return time

def request_date():
    date_correct = True
    while date_correct:
        try:
            date_entry = input('Enter a date in MM-DD-YYYY format\n')
            month, day, year = map(int, date_entry.split('-'))
            date = datetime.date(year, month, day)
            if date < datetime.date.today():
                print("Date is invalid\n")
                continue
            date_correct = False
        except:
            print("Date is not defined, try again.\n")
    
    return date

def compare_time():
    time_compare = False
    while not time_compare:
        startTime = request_time('Start')
        endTime = request_time('End')
        if endTime > startTime:
            time_compare = True
        else:
            print("Start time must be before End Time\n")

    return startTime, endTime

def compare_datetime(entire_schedule, curr_date, curr_start, curr_end):
    # all of the dates in the schedule
    dates = [ history['date'] for history in entire_schedule]
    print(dates)
    datetime_compare = False
    while not datetime_compare:
        # change curr_date to string of format MM-DD-YYYY so it can compare with dates
        # need to change start and end arrays into date/time format
        if (curr_date in dates):
             # all of the starts in the schedule
            starts = [ history['start'] for history in entire_schedule if history.get('date') == curr_date]
            print(starts)
            # all of the end times in the schedule
            ends = [ history['end'] for history in entire_schedule if history.get('date') == curr_date]
            print(ends)

            for i in range (len(starts)):
                if (curr_start < starts[i] and curr_end > starts[i] and curr_end < ends[i]):
                    print("conflict 1")
                elif(curr_start > starts[i] and curr_start < ends[i] and curr_end > ends[i]):
                    print("conflict 2")
                elif(curr_start > starts[i] and curr_end < ends[i]):
                    print("conflict 3")
                elif(curr_start < starts[i] and curr_end > ends[i]):
                    print("conflict 4")
                else:
                    print("all good, cheerio mate")
            datetime_compare = True

        
                
                
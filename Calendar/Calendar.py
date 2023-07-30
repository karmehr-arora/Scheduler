import datetime

def create(Name, startTime, EndTime, Date, Repititions):
    print(Name)
    print(startTime)
    print(EndTime)
    print(Date)
    print(Repititions)

continues = True
while continues:
    val = input("__________________________________________________________\nSelect one of the following main menu option: \n [C]reate, [V]iew schedules, [D]elete Event, [Q]uit\n")
    val = val.upper()

    if val == 'Q':
        continues = False
        print("\nQuitting...")

    elif val == 'C':
        name = input("Name of Event: \n")
        startTime = input("Start Time: \n")
        endTime = input("End Time: \n")
        date_correct = True
        date1 = datetime.date.today()
        while date_correct:
            try:
                date_entry = input('Enter a date in MM-DD-YYYY format\n')
                month, day, year = map(int, date_entry.split('-'))
                date1 = datetime.date(year, month, day)
                if date1 < datetime.date.today():
                    print("Date is invalid")
                    continue
                date_correct = False
            except:
                print("\nDate is not defined, try again.\n")

        repeat = input("Would you like to repeat this event [N]one, [D]aily, [W]eekly, [M]onthly, [Y]early\n")
        
        create(name, startTime, endTime, date1, repeat)

    elif val == "D":
        print("Deleting")

    elif val == "V":
        print("Viewing")

    else:
        print("\nError: Incorrect Input Format")
print("done")
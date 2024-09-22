import sys
from datetime import datetime, timedelta


def clockOut(timesheet_file, date_and_time):

    last_entry = list(timesheet_file.readlines()[-1].split())
    last_entry_datetime = datetime.strptime(last_entry[0], "%b/%d/%y-%I:%M%p")
    hours_passed = round((date_and_time - last_entry_datetime) / timedelta(hours=1), 2)
    timesheet_file.seek(0)

    current_data = "\n".join(timesheet_file.read().split("\n")[:-2])
    timesheet_file.seek(0)

    if len(last_entry) == 1:
        date_and_time_string = date_and_time.strftime("%b/%d/%y-%I:%M%p")

        new_entry = "\t".join((last_entry[0], date_and_time_string, str(hours_passed)))

        # Prevent the first clockout of the file to add an unnecessary
        if len(current_data) == 0:
            timesheet_file.write(current_data + new_entry + "\n")
        else:
            timesheet_file.write(current_data + "\n" + new_entry + "\n")

        timesheet_file.truncate()

    else:
        print("Last entry in timesheet file already has a clockout")
        timesheet_file.close()
        sys.exit(1)
    print("\U0001F554", "Clocked-Out", "\U0001F554")

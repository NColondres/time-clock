# parse the entire timesheet file and calculate hours if they have a start & end date (missing hours field).
from datetime import datetime, timedelta

def patch_file(timesheet_file):

    lines_to_write = []
    
    line_number = 0

    for line in timesheet_file:
        line_number += 1
        line_data = line.split()

        
        # If the line only has a clock-in and clock-out. Then calculate the hours
        if len(line_data) == 2:

            clockin_date = datetime.strptime(line_data[0], "%b/%d/%y-%I:%M%p")
            clockout_date = datetime.strptime(line_data[1], "%b/%d/%y-%I:%M%p")
            hours_passed = round((clockout_date - clockin_date) / timedelta(hours=1), 2)

            clockin_date = clockin_date.strftime("%b/%d/%y-%I:%M%p")
            clockout_date = clockout_date.strftime("%b/%d/%y-%I:%M%p")
            hours_passed = str(hours_passed)

            replacement_line = "   ".join([clockin_date, clockout_date, hours_passed]) + "\n"

            lines_to_write.append(replacement_line)

            print(f"Patched line {line_number}:\n  {replacement_line}")

        else:
            lines_to_write.append(line)
    
    timesheet_file.seek(0)
    timesheet_file.writelines(lines_to_write)
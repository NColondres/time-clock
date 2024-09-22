from datetime import datetime


def hours_weekly(timesheet_file, week_offset=0):
    hours_worked = 0

    desired_week = datetime.now().isocalendar()[1] + week_offset
    print(desired_week)

    for line in timesheet_file:
        line_data = line.rstrip("\n").split("\t")

        if len(line_data) < 3:
            print(f"Skipping entry: {"\t".join(line_data)} as it is incomplete.")

        else:
            starting_date = datetime.strptime(line_data[0], "%b/%d/%y-%I:%M%p")

            if starting_date.isocalendar()[1] == desired_week:

                hours_worked += float(line_data[2])

    print("\U000023F3", hours_worked, "\U0000231B")

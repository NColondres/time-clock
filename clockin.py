def clockIn(timesheet_file, date_and_time):

    timesheet_file.seek(0, 2)

    date_and_time_string = date_and_time.strftime("%b/%d/%y-%I:%M%p\n")
    timesheet_file.write(date_and_time_string)

    print("\U0001F558", "Clocked-In", "\U0001F558")

#!/usr/bin/env python3
import sys
import os.path
import clockin, clockout, hours_weekly, patch_file
from datetime import datetime


def main():
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    TIMESHEET_LOCATION = f"{ROOT_PATH}/timesheet"
    DATE_AND_TIME = datetime.now()

    argument = sys.argv[1].lower()

    # Open timesheet file
    if os.path.isfile(TIMESHEET_LOCATION):
        timesheet_file = open(TIMESHEET_LOCATION, "r+")
    else:
        print("File does not exist. Creating new timesheet file.")
        timesheet_file = open(TIMESHEET_LOCATION, "w+")

    available_cmds = ["clockin", "clockout", "week", "patch"]

    if argument in available_cmds:
        match argument:
            case "clockin":
                clockin.clockIn(timesheet_file, DATE_AND_TIME)

            case "clockout":
                clockout.clockOut(timesheet_file, DATE_AND_TIME)

            case "patch":
                patch_file.patch_file(timesheet_file)
                timesheet_file.close()

            case "week":
                if len(sys.argv) < 3:
                    hours_weekly.hours_weekly(timesheet_file)
                elif not sys.argv[2].strip("-").isdigit():
                    print("Second Argument not an int value")
                    timesheet_file.close()
                    sys.exit(1)
                elif int(sys.argv[2]) > 0:
                    print("Must be 0 or negative number. Can't see into the future")
                    timesheet_file.close()
                    sys.exit(1)
                else:
                    offset_argument = int(sys.argv[2])
                    hours_weekly.hours_weekly(timesheet_file, offset_argument)

    else:
        print(
            f"Argument not one of available commands\nAvailable cmds: {" ".join(available_cmds)}"
        )
        timesheet_file.close()
        sys.exit(1)


if __name__ == "__main__":
    main()

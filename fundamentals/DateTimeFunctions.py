from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    today = date.today()
    print("Today: " + str(today))
    print("Day:" + str(today.day) + " Month:" + str(today.month) + " Year:" + str(today.year))

    now = datetime.now()
    print("Default datetime now format: " + str(now))
    print("Current date time: " + now.ctime())
    print("Hour:" + str(now.hour) + " Minute:" + str(now.minute) + " Second:" + str(now.second))
    print("Short date format: " + now.strftime("%D"))
    print("Day format: " + now.strftime("%d"))
    print("Short month format: " + now.strftime("%b"))
    print("Long month format: " + now.strftime("%B"))
    print("Short year format: " + now.strftime("%y"))
    print("Long year format: " + now.strftime("%Y"))
    print("Short day format: " + now.strftime("%a"))
    print("Long day format: " + now.strftime("%A"))

    # %c - local date and time, %x-local's date, %X- local's time
    print(now.strftime("%c"))
    print(now.strftime("%x"))
    print(now.strftime("%X"))

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
    print(now.strftime("%I:%M:%S %p"))  # 12-Hour:Minute:Second:AM
    print(now.strftime("%H:%M"))  # 24-Hour:Minute

    new_year_day = date(today.year, 1, 1)
    if new_year_day < today:
        print("New Year celebration is over %d days." % (today - new_year_day).days)

    print()


if __name__ == "__main__":
    main()

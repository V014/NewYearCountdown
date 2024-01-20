from datetime import datetime, timedelta

def new_year_countdown():
    current_time = datetime.now()
    new_year = datetime(current_time.year + 1, 1, 1, 0, 0, 0)

    time_remaining = new_year - current_time
    print(f"Time until New Year: {time_remaining}")

# call the function to see the countdown
new_year_countdown()
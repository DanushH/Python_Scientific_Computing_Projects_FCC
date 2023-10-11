def add_time(start, duration, start_day=None):
    days_of_week = {
        "sunday": 0,
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
    }

    start = start.split()
    start_hrs, start_mins = map(int, start[0].split(":"))
    am_pm = start[1]
    if am_pm == "PM":
        start_hrs += 12

    duration_hrs, duration_mins = map(int, duration.split(":"))

    start_time_in_mins = start_hrs * 60 + start_mins
    duration_in_mins = duration_hrs * 60 + duration_mins
    print(start_time_in_mins, duration_in_mins)

    end_time_in_mins = start_time_in_mins + duration_in_mins
    end_hrs = end_time_in_mins // 60
    end_mins = end_time_in_mins % 60
    print(end_time_in_mins, end_hrs, end_mins)

    n_days_later = end_hrs // 24
    end_hrs %= 24

    print(end_hrs)
    if end_hrs >= 12:
        am_pm = "PM"
    if end_hrs < 12:
        am_pm = "AM"
    if end_hrs > 12:
        end_hrs -= 12
    if end_hrs == 0:
        end_hrs += 12

    if start_day:
        start_day = start_day.lower()
        end_day_index = (days_of_week[start_day] + n_days_later) % 7
        end_day = list(days_of_week.keys())[
            list(days_of_week.values()).index(end_day_index)
        ]
        end_time = f"{end_hrs}:{end_mins:02} {am_pm}, {end_day.capitalize()}"
    else:
        end_time = f"{end_hrs}:{end_mins:02} {am_pm}"

    if n_days_later == 1:
        end_time += " (next day)"
    elif n_days_later > 1:
        end_time += f" ({n_days_later} days later)"

    return end_time

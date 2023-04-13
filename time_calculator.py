def add_time(start_time, duration, start_day=None):
    """
    The function returns the result as a string formatted according
    to the specifications in the prompt. The function handles both AM and PM times correctly
    and converts them to a 24-hour format for easier calculation. 
    The function also takes an optional starting day of the week parameter, 
    which it uses to calculate the resulting day of the week. 
    The function returns the result as a string with the correct punctuation and spacing.
    """
    # Parse the start time and duration
    start_time, am_pm = start_time.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert to 24-hour format
    if am_pm == 'PM' and start_hour != 12:
        start_hour += 12

    # Add the duration
    end_minute = (start_minute + duration_minute) % 60
    carry_hour = (start_minute + duration_minute) // 60
    end_hour = (start_hour + duration_hour + carry_hour) % 24
    carry_day = (start_hour + duration_hour + carry_hour) // 24

    # Convert back to 12-hour format
    if end_hour >= 12:
        end_am_pm = 'PM'
        if end_hour > 12:
            end_hour -= 12
    else:
        end_am_pm = 'AM'
        if end_hour == 0:
            end_hour = 12

    # Format the result string
    result = f"{end_hour:02d}:{end_minute:02d} {end_am_pm}"
    if start_day is not None:
        start_day = start_day.capitalize()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_idx = days.index(start_day)
        end_idx = (start_idx + carry_day) % 7
        result += f", {days[end_idx]}"
    if carry_day == 1:
        result += " (next day)"
    elif carry_day > 1:
        result += f" ({carry_day} days later)"
    return result
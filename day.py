import calendar

def dayname(time):
    """Return the name of the day of the week for the given time."""
    return calendar.day_name[time.weekday()]

def greeting(time):
    """Return a friendly greeting based on the given time."""
    return f"<p>Hello, Happy {dayname(time)} from a module!.</p>"
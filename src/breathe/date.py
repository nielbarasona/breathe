import datetime


def format_date(date: datetime.date) -> str:
    return date.strftime("%A %d. %B %Y")

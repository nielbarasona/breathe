import datetime as dt

from .date import format_date


class Part:
    def __init__(self, name: str, date: dt.date, interval: int) -> None:
        self.name = name
        self.date = date
        self.interval = interval
        self.next_event = self.date + dt.timedelta(days=self.interval)
        self.format = ("Name", "Date", "Interval", "Next Event")

    def __repr__(self) -> str:
        return f"Name: {self.name} Date: {format_date(self.date)} Interval: {self.interval} Next Event: {format_date(self.next_event)}"

    def output(self) -> tuple:
        return (self.name, self.date, self.interval, self.next_event)

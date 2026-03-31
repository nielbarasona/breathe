import datetime as dt
from breathe.part import Part


def test_part_creation():
    date = dt.date.fromisoformat("20261105")
    part = Part("Test", date, 30)
    assert (
        repr(part)
        == "Name: Test Date: Thursday 05. November 2026 Interval: 30 Next Event: Saturday 05. December 2026"
    )

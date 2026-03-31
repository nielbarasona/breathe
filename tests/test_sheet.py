import datetime as dt
from breathe.part import Part
from breathe.sheet import Sheet


def test_sheet_creation():
    part = Part("Test", dt.date.fromisoformat("2026-11-05"), 30)
    sheet = Sheet()
    sheet.parts.append(part)
    assert (
        repr(sheet)
        == "Name: Test Date: Thursday 05. November 2026 Interval: 30 Next Event: Saturday 05. December 2026"
    )

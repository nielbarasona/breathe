import datetime as dt
from .part import Part
from .sheet import Sheet
from .tui import BreatheApp


def main():
    sheet = Sheet()
    part = Part("Test", dt.date.fromisoformat("2026-11-05"), 30)
    part2 = Part("Test2", dt.date.fromisoformat("2026-06-02"), 30)
    sheet.parts.append(part)
    sheet.parts.append(part2)

    app = BreatheApp(sheet)
    app.run()


if __name__ == "__main__":
    main()

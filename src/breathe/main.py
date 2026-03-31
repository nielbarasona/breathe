import datetime as dt
from .part import Part
from .sheet import Sheet


def main():
    sheet = Sheet()
    part = Part("Test", dt.date.fromisoformat("2026-11-05"), 30)
    part2 = Part("Test2", dt.date.fromisoformat("2026-06-02"), 30)
    sheet.parts.append(part)
    sheet.parts.append(part2)
    print(sheet)

    # input_date = input("Enter the date (format: YYYY-MM-DD): ")
    # date = dt.date.fromisoformat(input_date)
    # input_name = input("Enter event Name: ")
    # user_event = Part(input_name, date, 30)
    #
    # print(user_event)


if __name__ == "__main__":
    main()

import datetime as dt
from .part import Part


def main():
    input_date = input("Enter the date (format: YYYYMMDD): ")
    date = dt.date.fromisoformat(input_date)
    input_name = input("Enter event Name: ")
    user_event = Part(input_name, date, 30)

    print(user_event)


if __name__ == "__main__":
    main()

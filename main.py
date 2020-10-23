from _datetime import datetime

from comparator import Comparator


def main():
    station = 'Działoszyn - PM10'
    from_datetime = datetime(year=2020, month=3, day=1, hour=0, minute=0)
    to_datetime = datetime(year=2020, month=3, day=31, hour=23, minute=0)
    comparator = Comparator(station, from_datetime, to_datetime)
    comparator.compare()
    comparator.plot()


if __name__ == '__main__':
    main()
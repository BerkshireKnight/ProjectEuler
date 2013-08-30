#!/usr/bin/env python

import calendar


def main():
    sunday_count = 0
    for year in range(1901,2001):
        for month in range(1,13):
            if calendar.weekday(year,month,1) == 6:
                sunday_count += 1

    print sunday_count


if __name__ == "__main__":
    main()

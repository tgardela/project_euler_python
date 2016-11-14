import timeit

def count_days(start_year, end_year):
    days_in_no_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day_counter = 1
    sunday_the_1st_counter= 0
    for year in range(start_year, end_year):
        if is_leap_year(year):
            days_in_month  = days_in_leap_year
        else:
            days_in_month = days_in_no_leap_year
        for month in range(0, 12):
            day_of_month = 1
            if day_counter % 7 == 0 and day_of_month == 1: sunday_the_1st_counter += 1
            for day in range(1, days_in_month[month] + 1):
                day_of_month += 1
                day_counter += 1
    return sunday_the_1st_counter - 1


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0: return False
        else: return True
    else: return False


def get_number_of_days_per_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0: return 365
        else: return 366
    else: return 365


if __name__=="__main__":
    start = timeit.default_timer()

    print(count_days(1901, 2001))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")


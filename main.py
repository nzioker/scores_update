from operations import Football


todays_date = Football.get_todays_date()

if __name__ == '__main__':
    Football(todays_date,2022,39).check_league()
    Football(todays_date,2022,2).check_league()
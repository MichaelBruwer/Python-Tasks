def age_program():
    seconds_or_years = input('secs (s) or years (y)')
    if seconds_or_years == 's':
        user_value = input('enter the number of seconds you have lived')
        print('you lived for {} years'.format(int(user_value) / 60 / 60 / 24 / 365))
    elif seconds_or_years == 'y':
        user_value = input('enter number of years you have lived')
        print('you lived {} seconds'.format(int(user_value) * 365 * 24 * 60 * 60))
age_program()
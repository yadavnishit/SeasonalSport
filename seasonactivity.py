# Season and Activity Suggestion according to time
season = input('Enter Season :').lower()
if season == 'summer':
    time = input('Enter time :').lower()
    if time == 'morning':
        print('swimming')
    elif time == 'evening':
        print('cricket')
    else:
        print('Provide Correct time ')
elif season == 'winter':
    time = input('Enter time :').lower()
    if time == 'morning':
        print('cricket')
    else:
        print('badminton')
elif season == 'rainy':
    time = input('Enter time :').lower()
    if time == 'morning':
        print('Football')
    else:
        print('Indoor Games')
else:
    print('Enter the correct season name!')
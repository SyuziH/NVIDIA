from constants import Times

def time_convert(time):
    hour, minute = map(int, time.split(':'))
    return hour + minute / 60

def correct_time_for_eat(user_time):
    time = time_convert(user_time)
    if Times.breakfast_start <= time <= Times.breakfast_end:
        return "It's time for Breakfast"
    if Times.lunch_start <= time <= Times.lunch_end:
        return "It's time for Lunch"
    if Times.dinner_start <= time <= Times.dinner_end:
        return "It's time for Dinner"
    else:
        return


user_time = input('Enter the time: ')
print(correct_time_for_eat(user_time))

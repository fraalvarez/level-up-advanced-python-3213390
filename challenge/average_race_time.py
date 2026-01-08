# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    
    jennifer_times = [re.findall('[\d]{1,2}:[\d]{1,2}[\.\d]{0,4}', x)[0] for x in races.splitlines() if 'Jennifer Rhines' in x]
    
    # print(jennifer_times)
    return jennifer_times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total_time = datetime.timedelta(0,0,0,0,0,0,0)

    for racetime in racetimes:
        if '.' in racetime:
            parsed = datetime.datetime.strptime(re.findall('[\d]{1,2}:[\d]{1,2}[\.\d]{0,4}', racetime)[0], "%M:%S.%f")
        else:
            parsed = datetime.datetime.strptime(re.findall('[\d]{1,2}:[\d]{1,2}', racetime)[0], "%M:%S")

        delta = datetime.timedelta(minutes=parsed.minute, seconds=parsed.second, milliseconds=parsed.microsecond)
        total_time += delta

    return f'{total_time / len(racetimes)}'[2:-5]

# print(get_average())
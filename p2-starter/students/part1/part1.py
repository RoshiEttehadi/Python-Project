import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    return f'{temp}{DEGREE_SYBMOL}'

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%d %H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

def convert_f_to_c(temp_in_farenheit):
    celcius = (temp_in_farenheit - 32) * 5 / 9
    return celcius

def calculate_mean(total, num_items):
    mean = total / num_items
    return(mean)

def process_weather(forecast_file):
    with open('forecast_5days_a.json') as forecast_file:
        data = json.load(forecast_file)

# The overall min temperature, 

for weather in data ['DailyForecasts']:
    overall_min_temp_f = min(weather["Temperature"]["Minimum"]["Value"])
    overall_min_temp_c = convert_f_to_c(overall_min_temp_f)
    overall_min_temp = format_temperature(overall_min_temp_c)

# and the date this will occur.
    date = convert_date(weather["Date"])
    if overall_min_temp_f == (weather["Temperature"]["Minimum"]["Value"]):
       low_day = (date) 

# The overall max temperature, 
    overall_max_temp_f = max(weather["Temperature"]["Maximum"]["Value"])
    overall_max_temp_c = convert_f_to_c(overall_max_temp_f)
    overall_max_temp = format_temperature(overall_max_temp_c)

# and the date this will occur.
    date = convert_date(weather["Date"])
    if overall_max_temp_f == (weather["Temperature"]["Minimum"]["Value"]):
       high_day = (date) 

# The mean minimum temperature.
    total = sum(weather["Temperature"]["Minimum"]["Value"])
    num_items = len(weather["Temperature"]["Minimum"]["Value"])
    mean_min_f = calculate_mean(total, num_items)
    mean_min_c = convert_f_to_c(mean_min_f)
    mean_min = format_temperature(mean_min_c)

# The mean maximum temperature.
    total = sum(weather["Temperature"]["Maximun"]["Value"])
    num_items = len(weather["Temperature"]["Maximum"]["Value"])
    mean_min_f = calculate_mean(total, num_items)    
    mean_max_c = convert_f_to_c(mean_max_f)
    mean_max = format_temperature(mean_max_c)

    print('5 Day Overview')
    print(f'\tThe lowest temperature will be {overall_min_temp}, and will occur on {low_day}')    
    print(f'\tThe highest temperature will be {overall_max_temp}, and will occur on {high_day}')  
    print(f'\tThe average low this week is {mean_min}') 
    print(f'\tThe average high this week is {mean_max}\n')

# A summary of each day:
for weather in data['DailyForecasts']:
    date = convert_date(weather["Date"])
    min_temp_f = (weather["Temperature"]["Minimum"]["Value"])
    min_temp_c = convert_f_to_c(min_temp_f)
    min_temp = format_temperature(min_temp_c)
    max_temp_f = (weather["Temperature"]["Maximum"]["Value"])
    max_temp_c = convert_f_to_c(max_temp_f)
    max_temp = format_temperature(max_temp_c)
    desc = (weather["Day"]["LongPhrase"])
    rain_chance = (weather["Day"]["RainProbability"])
    desc_pm = (weather["Night"]["LongPhrase"])
    rain_chance_pm = (weather["Night"]["RainProbability"])


    print(f'-------- {date} --------')
    print(f'Minimum Temperature: {min_temp}')
    print(f'Maximum Temperature: {max_temp}')
    print(f'Daytime: {desc}\n\tChance of rain:\t {rain_chance}%')
    print(f'Nighttime: {desc_pm}\n\tChance of rain:\t {rain_chance_pm}%\n')

    
if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))






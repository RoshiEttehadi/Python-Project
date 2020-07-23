import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# Takes a temperature and returns it in string format with the degrees and celcius symbols.
def format_temperature(temp):
    return f'{temp}{DEGREE_SYBMOL}'

# Converts and ISO formatted date into a human readable format.
def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

# Converts an temperature from farenheit to celcius.
def convert_f_to_c(temp_in_farenheit):
    num = (temp_in_farenheit - 32) * 5 / 9
    celcius = round(num, 1)
    return celcius

# Calculates the mean.
def calculate_mean(total, num_items):
    mean = round((total / num_items), 1) 
    return mean

# Converts raw weather data into meaningful text.
def process_weather(forecast_file):
    with open(forecast_file, encoding="utf8") as f:
        data = json.load(f)
        
    # The overall min temperature, 
    min_temp = []
    date = []
    max_temp = []
    desc = []
    rain_chance = []
    desc_pm = []
    rain_chance_pm = []

    for weather in data['DailyForecasts']:
        min_temp.append(convert_f_to_c(
            weather["Temperature"]["Minimum"]["Value"]))
        max_temp.append(convert_f_to_c(
            weather["Temperature"]["Maximum"]["Value"]))
        date.append(convert_date(weather["Date"]))   
        # A summary of each day:
        desc.append(weather["Day"]["LongPhrase"])
        rain_chance.append(weather["Day"]["RainProbability"])
        desc_pm.append(weather["Night"]["LongPhrase"])
        rain_chance_pm.append(weather["Night"]["RainProbability"])

    # The mean minimum temperature.
    mean_min_c = calculate_mean(sum(min_temp), len(min_temp))
    mean_min = format_temperature(mean_min_c)

    # The mean maximum temperature.
    mean_max_c = calculate_mean(sum(max_temp), len(max_temp))
    mean_max = format_temperature(mean_max_c)
        
    # and the date this will occur.
    min_index = min_temp.index(min(min_temp))
    low_day = date[min_index]

    # and the date this will occur.
    max_index = max_temp.index(max(max_temp))
    high_day = date[max_index]

    final_output = f"""{len(date)} Day Overview
    The lowest temperature will be {format_temperature(min(min_temp))}, and will occur on {low_day}.
    The highest temperature will be {format_temperature(max(max_temp))}, and will occur on {high_day}.
    The average low this week is {mean_min}.
    The average high this week is {mean_max}.\n"""

    x = 0
    while x!= len(date):
        final_output += f"""\n-------- {date[x]} --------
Minimum Temperature: {format_temperature(min_temp[x])}
Maximum Temperature: {format_temperature(max_temp[x])}
Daytime: {desc[x]}
    Chance of rain:  {rain_chance[x]}%
Nighttime: {desc_pm[x]}
    Chance of rain:  {rain_chance_pm[x]}%
"""
        x = x + 1

    final_output = final_output + "\n"

    with open(f"forecast_{len(date)}days_output.txt", "w", encoding="utf8") as txt_file:
        txt_file.write(final_output)
    return final_output
    
if __name__ == "__main__":
    # print(process_weather("data/forecast_5days_a.json"))
    print(process_weather("data/forecast_5days_b.json"))
    # print(process_weather("data/forecast_10days.json"))
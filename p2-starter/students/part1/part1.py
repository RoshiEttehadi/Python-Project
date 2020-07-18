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
    celcius = round((temp_in_farenheit - 32) * 5 / 9)
    return celcius

# Calculates the mean.
def calculate_mean(total, num_items):
    mean = round(total / num_items)
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
        min_temp.append(convert_f_to_c(weather["Temperature"]["Minimum"]["Value"]))
        max_temp.append(convert_f_to_c(weather["Temperature"]["Maximum"]["Value"]))
        date.append(convert_date(weather["Date"]))   
        # A summary of each day:
        desc.append(weather["Day"]["LongPhrase"])
        rain_chance.append(weather["Day"]["RainProbability"])
        desc_pm.append(weather["Night"]["LongPhrase"])
        rain_chance_pm.append(weather["Night"]["RainProbability"])

        # The mean minimum temperature.
        mean_min_c = sum(min_temp) / len(min_temp)
        mean_min = format_temperature(mean_min_c)

        # The mean maximum temperature.
        mean_max_c = sum(max_temp) / len(max_temp)
        mean_max = format_temperature(mean_max_c)
        
    # and the date this will occur.
    min_index = min_temp.index(min(min_temp))
    low_day = date [min_index]

    # and the date this will occur.
    max_index = max_temp.index(max(max_temp))
    high_day = date [max_index]

    final_output1 = f"""5 Day Overview\n\tThe lowest temperature will be {min(min_temp)}, and will occur on {low_day}\n\tThe highest temperature will be {max(max_temp)}, and will occur on {high_day}\n\tThe average low this week is {mean_min}\n\tThe average high this week is {mean_max}\n"""

    final_output2 = ""
    for x in range(5):
        final_output2 = final_output2 + (f"""-------- {date[x]} --------\nMinimum Temperature: {min_temp[x]}\nMaximum Temperature: {max_temp[x]}\nDaytime: {desc[x]}\n\tChance of rain:\t {rain_chance[x]}%\nNighttime: {desc_pm[x]}\n\tChance of rain:\t {rain_chance_pm[x]}%\n""")
    final_final_output = final_output1 + final_output2    
    return final_final_output

    
if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    # print(process_weather("data/forecast_5days_b.json"))
    # print(process_weather("data/forecast_10days.json"))
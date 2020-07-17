import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    pass


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    pass


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    pass


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))



# def process_weather(forecast_file):
#     with open(forecast_file) as json_file:
#         json_data = json.load(json_file)
#         highest_temp = 0
#         lowest_temp = 50
#         max_mean_calc = 0
#         min_mean_calc = 0
#         num_items = 0
#         line = []

#     for weather in json_data['DailyForecasts']:
#         #gather number of days, and dates
#         num_items = num_items + 1

#         date_input = (weather["Date"])
#         date = convert_date(date_input)
#         #calculate minimum 
#         min_temp_f = (weather["Temperature"]["Minimum"]["Value"])
#         min_temp_c = convert_f_to_c(min_temp_f)
#         #adds values to preform calc
#         min_mean_calc = min_mean_calc + min_temp_c
#         #returns calculated & formatted mean
#         low_mean = calculate_mean(min_mean_calc, num_items)

#         #determines lowest temp & day
#         if min_temp_c < lowest_temp:
#             lowest_temp = min_temp_c
#             low_day = (date)
#             low_day_temp = format_temperature(min_temp_c)


#         #calculate minimum 
#         max_temp_f = (weather["Temperature"]["Maximum"]["Value"])
#         max_temp_c = convert_f_to_c(max_temp_f)
#         #adds values to preform calc
#         max_mean_calc = max_mean_calc + max_temp_c
#         #returns calculated & formatted mean
#         high_mean = calculate_mean(max_mean_calc, num_items)
#         #determines lowest temp & day
#         if max_temp_c > highest_temp:
#             highest_temp = max_temp_c
#             high_day = (date)
#             high_day_temp = format_temperature(max_temp_c)


#         with open("test.txt", "w") as txt_file:
#             txt_file.write(f"{num_items} Day Overview \n")
#             txt_file.write(f"\tThe lowest temperature will be {low_day_temp}, and will occour on {low_day}.\n")
#             txt_file.write(f"\tThe highest temperature will be {high_day_temp}, and will occour on {high_day}.\n")
#             txt_file.write(f"\tThe average low this week is {low_mean}.\n")
#             txt_file.write(f"\tThe average high this week is {high_mean}.\n\n")


#     with open("test.txt", "a") as txt_file: 
#         for weather in json_data['DailyForecasts']:
#             min_temp_f = (weather["Temperature"]["Minimum"]["Value"])
#             min_temp_c = convert_f_to_c(min_temp_f)
#             max_temp_f = (weather["Temperature"]["Maximum"]["Value"])
#             max_temp_c = convert_f_to_c(max_temp_f)
#             date_input = (weather["Date"])
#             date = convert_date(date_input)
#             long_man = (weather["Day"]["LongPhrase"])
#             rain_chance = (weather["Day"]["RainProbability"])
#             long_man_pm = (weather["Night"]["LongPhrase"])
#             rain_chance_pm = (weather["Night"]["RainProbability"])
#             max_temp = format_temperature(max_temp_c)
#             min_temp = format_temperature(min_temp_c)
            
#             txt_file.write(f"-------- {date} --------\n")
#             txt_file.write(f"Minimum Temperature: {min_temp}\n")
#             txt_file.write(f"Maximum Temperature: {max_temp}\n")
#             txt_file.write(f"Daytime: {long_man} \n\tChance of rain:\t {rain_chance}%\n")
#             txt_file.write(f"Nighttime: {long_man_pm} \n\tChance of rain:\t {rain_chance_pm}%\n\n")

#     # txt_file.close()


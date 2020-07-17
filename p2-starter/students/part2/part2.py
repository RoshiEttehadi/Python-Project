import json
import plotly.express as px

with open (forecast_file, encoding="utf8") as json_file:
    data = json.load(json_file)

df = pd.read_json("forecast_file")
# A single time series graph that contains both the minimum and maximum temperatures for each day.
df = {
    "days": convert_date (["DailyForecasts"]["Date"])
    "Min_temp": ["DailyForecasts"]["Temperature"]["Minimum"]["Value"]
    "Max_temp": ["DailyForecasts"]["Temperature"]["Maximum"]["Value"]
}
fig = px.line(
df,
x="days",
y="Min_temp",
z="Max_temp"
title='Forecast Graphs'
)
fig.show()
# A single time series graph that contains the minimum, minimum “real feel”, and minimum “real feel
# shade” temperatures.
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Forecast Graphs')
fig.show()
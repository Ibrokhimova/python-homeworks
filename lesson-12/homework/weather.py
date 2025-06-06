from bs4 import BeautifulSoup
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
rows = soup.select("tbody tr")
forecast = []
for row in rows:
    cells = row.find_all("td")
    day = cells[0].text.strip()
    temp = int(cells[1].text.strip().replace("°C", ""))
    condition = cells[2].text.strip()
    forecast.append((day, temp, condition))
print(" 5-Day Weather Forecast:")
for day, temp, condition in forecast:
    print(f"{day}: {temp}°C, {condition}")
max_temp = max(forecast, key=lambda x: x[1])[1]
hottest_days = [day for day, temp, _ in forecast if temp == max_temp]
sunny_days = [day for day, _, condition in forecast if condition.lower() == "sunny"]
average_temp = sum(temp for _, temp, _ in forecast) / len(forecast)
print(f"\n Highest Temperature: {max_temp}°C on {', '.join(hottest_days)}")
print(f" Sunny Days: {', '.join(sunny_days)}")
print(f" Average Temperature: {average_temp:.1f}°C")
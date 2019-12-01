import sys
from pogoda import wypisz_id, get_location_weather, prepare_weather_report
print(sys.argv)
if len(sys.argv) > 1:
    location_name = sys.argv[1]
    print(wypisz_id(location_name))

if len(sys.argv) > 1:
    location_name = sys.argv[1]
    location_id = wypisz_id(location_name)
    weather = get_location_weather(location_id)
    print(prepare_weather_report(weather, location_name))

import requests
from django.shortcuts import render
from .forms import CityForm
from datetime import datetime, timedelta

API_KEY = "fa8021383ce44a4f92f143915251509"
BASE_URL = "http://api.weatherapi.com/v1"

def weather_report(request):
    weather_cards = []
    future_cards = []
    error = None

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]

            try:
                today = datetime.today().date()
                yesterday = today - timedelta(days=1)
                tomorrow = today + timedelta(days=1)
                day_after = today + timedelta(days=2)

                # Yesterday
                res_yest = requests.get(f"{BASE_URL}/history.json?key={API_KEY}&q={city}&dt={yesterday}").json()
                if "forecast" in res_yest:
                    day = res_yest["forecast"]["forecastday"][0]["day"]
                    weather_cards.append({
                        "title": "Yesterday",
                        "date": str(yesterday),
                        "avg_temp": day["avgtemp_c"],
                        "max_temp": day["maxtemp_c"],
                        "min_temp": day["mintemp_c"],
                        "condition": day["condition"]["text"],
                        "icon": "https:" + day["condition"]["icon"],
                    })

                # Today + next 4 days
                res_forecast = requests.get(f"{BASE_URL}/forecast.json?key={API_KEY}&q={city}&days=5").json()
                if "forecast" in res_forecast:
                    loc = res_forecast["location"]
                    for d in res_forecast["forecast"]["forecastday"]:
                        date_obj = datetime.strptime(d["date"], "%Y-%m-%d").date()
                        day = d["day"]

                        if date_obj == today:
                            # Today
                            weather_cards.append({
                                "title": "Today",
                                "date": str(today),
                                "avg_temp": day["avgtemp_c"],
                                "max_temp": day["maxtemp_c"],
                                "min_temp": day["mintemp_c"],
                                "condition": day["condition"]["text"],
                                "icon": "https:" + day["condition"]["icon"],
                                "city": loc["name"],
                                "country": loc["country"],
                            })
                        elif date_obj == tomorrow:
                            weather_cards.append({
                                "title": "Tomorrow",
                                "date": str(date_obj),
                                "avg_temp": day["avgtemp_c"],
                                "max_temp": day["maxtemp_c"],
                                "min_temp": day["mintemp_c"],
                                "condition": day["condition"]["text"],
                                "icon": "https:" + day["condition"]["icon"],
                            })
                        elif date_obj == day_after:
                            weather_cards.append({
                                 "title": date_obj.strftime("%A"), 
                                "date": str(date_obj),
                                "avg_temp": day["avgtemp_c"],
                                "max_temp": day["maxtemp_c"],
                                "min_temp": day["mintemp_c"],
                                "condition": day["condition"]["text"],
                                "icon": "https:" + day["condition"]["icon"],
                            })
                        elif date_obj > day_after:
                            future_cards.append({
                                "title": date_obj.strftime("%A"),
                                "date": str(date_obj),
                                "avg_temp": day["avgtemp_c"],
                                "max_temp": day["maxtemp_c"],
                                "min_temp": day["mintemp_c"],
                                "condition": day["condition"]["text"],
                                "icon": "https:" + day["condition"]["icon"],
                            })

            except Exception as e:
                error = f"Could not fetch weather data. {e}"

    else:
        form = CityForm()

    return render(request, "weather.html", {
        "form": form,
        "weather_cards": weather_cards,
        "future_cards": future_cards,
        "error": error,
    })

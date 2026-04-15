from flask import Flask, render_template,request
import requests
import configparser

app = Flask(__name__)

@app.route('/')
def weather_data():
    return render_template("index.html")

@app.route('/weatherdata', methods=['POST'])
def weather_results():
        city_name = request.form['cityname']
        api_key = get_api_key()
        data = get_weather_data(city_name, api_key)
        try:

            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            min_temp = data['main']['temp_min']
            max_temp = data['main']['temp_max']
            main = data['weather'][0]['main']
            location = data['name']
            country = data['sys']['country']   
        except Exception:
            error = f"{city_name} is not a valid!"
            return error


        return render_template("results.html", 
            temp= temp,
            feels_like= feels_like,
            min_temp= min_temp,
            max_temp= max_temp,
            main= main,
            location= location,
            country= country
            )
        


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather_data(city_name, api_key):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
    res = requests.get(api_url)
    if res != "":
        return res.json()
    else:
        return city_name


def get_weather_forecast(city_name, api_key, days=5):
    """
    Fetch 5-day weather forecast for a city.
    
    Args:
        city_name: Name of the city
        api_key: OpenWeatherMap API key
        days: Number of days (max 5)
    
    Returns:
        dict: Forecast data with daily predictions
    """
    api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={api_key}"
    res = requests.get(api_url)
    if res.status_code == 200:
        data = res.json()
        # Process forecast data - group by day
        daily_forecast = []
        current_day = None
        day_data = []
        
        for item in data['list']:
            date = item['dt_txt'].split(' ')[0]
            if date != current_day:
                if day_data:
                    daily_forecast.append({
                        'date': current_day,
                        'temps': [d['temp'] for d in day_data],
                        'weather': day_data[0]['weather'],
                        'avg_temp': sum(d['temp'] for d in day_data) / len(day_data)
                    })
                current_day = date
                day_data = []
            
            day_data.append({
                'temp': item['main']['temp'],
                'weather': item['weather'][0]['main']
            })
        
        return {
            'city': data['city']['name'],
            'country': data['city']['country'],
            'forecast': daily_forecast[:days]
        }
    else:
        return {'error': f'Failed to fetch forecast for {city_name}'}


@app.route('/forecast', methods=['GET', 'POST'])
def forecast_results():
    """Display 5-day weather forecast for a city."""
    if request.method == 'POST':
        city_name = request.form.get('cityname', '')
        days = int(request.form.get('days', 5))
    else:
        city_name = request.args.get('city', '')
        days = int(request.args.get('days', 5))
    
    if not city_name:
        return render_template("forecast.html", error="Please provide a city name")
    
    api_key = get_api_key()
    forecast_data = get_weather_forecast(city_name, api_key, days)
    
    if 'error' in forecast_data:
        return render_template("forecast.html", error=forecast_data['error'])
    
    return render_template("forecast.html", 
                          forecast=forecast_data,
                          city=city_name,
                          days=days)


if __name__=="__main__":
    app.run(debug=True)

# To Trigger Other Workflow
# Add secrets like (ANTHROPIC_API_KEY, DOCS_REPO_TOKEN)
# Merge your test PR to main with code changed
# The doc automation will run automatically ok.
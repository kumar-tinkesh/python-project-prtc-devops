from flask import Flask, render_template, request, jsonify
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





@app.route('/api/weather/<city>', methods=['GET'])
def api_weather(city):
    """
    REST API endpoint to get weather data for a city.
    Returns JSON response with current weather.
    """
    api_key = get_api_key()
    data = get_weather_data(city, api_key)
    
    if isinstance(data, dict) and 'main' in data:
        return jsonify({
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'weather': data['weather'][0]['main'],
            'description': data['weather'][0]['description']
        })
    else:
        return jsonify({'error': f'Could not fetch weather for {city}'}), 404


if __name__=="__main__":
    app.run(debug=True)

# To Trigger Other Workflow
# Add secrets like (ANTHROPIC_API_KEY, DOCS_REPO_TOKEN)
# Merge your test PR to main with code changed
# The doc automation will run automatically ok.# Feature mapping test 1776241590

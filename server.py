from flask import Flask, render_template, request,redirect
import weather
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/weather.html')
def weather_page(w=weather.get_weather_info()):
    return render_template("weather.html", w=w)


@app.route('/get_weather', methods=['POST', 'GET'])
def get_weather():
    if request.method == "POST":
        try:
            #weather_info = weather.get_weather_info()
            return redirect("/weather.html")
            
        except:
            return "error"
    else:
        return None


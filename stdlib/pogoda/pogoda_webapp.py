from flask import Flask, render_template

from pogoda import wypisz_id, get_location_weather, prepare_weather_report

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite://C:\Users\kurs\workspace\Python_bootcamp\stdlib\pogoda\test.db'
db = SQLAlchemy(app)
@app.route("/")
def index():
    return "My Weather Page"

@app.route('/<location_name>')
def weather(location_name):
    location_id = wypisz_id(location_name)
    weather = get_location_weather(location_id)
    lista = [x**2 for x in range(10)]
    return render_template("index.html", weather=weather, lista=lista)

@app.route('/history/download')
def h

@app.route('/history')
def history():



class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.Text, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Text, nullable=False)

#     weather_report = f"""<html>
#     <head></head>
#     <body>
#     <table>
#     <tr>
#         <td>Lokalizacja</td>
#         <td>{location_name}</td>
#     </tr>
#     <tr>
#         <td>Średnia temperatura</td>
#         <td>{weather.the_temp}</td>
#     </tr>
#     <tr>
#         <td>Wilgotność powietrza</td>
#         <td>{weather.humidity}</td>
#     </tr>
#     </table>
#     </body>
# </html>"""
#     #weather_report = prepare_weather_report(weather, location_name)
#
#     return weather_report
if __name__ == "__main__":
    app.run()
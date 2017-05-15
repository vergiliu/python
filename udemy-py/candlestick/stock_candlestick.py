import datetime

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import CDN
from flask import Flask, render_template
from pandas_datareader import data

app = Flask(__name__)


@app.route('/<symbol_name>')
@app.route('/<symbol_name>/<string:start_date>')
def plot(symbol_name, start_date=None):
    if start_date:
        print("date={}".format(start_date))
        # %Y  Year with century as a decimal number.
        # %m  Month as a decimal number [01,12].
        # %d  Day of the month as a decimal number [01,31].
        start_moment = datetime.datetime.strptime(start_date, "%d%m%Y")
    else:
        print("no start moment given, last 10 days")
        start_moment = datetime.date.today() - datetime.timedelta(days=10)
    end_moment = datetime.datetime.today()

    if not symbol_name:
        symbol_name = "GOOG"
    my_data = data.DataReader(name=symbol_name, data_source="yahoo", start=start_moment, end=end_moment)

    def inc_dec(c, o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"
        return value

    my_data["Status"] = [inc_dec(c, o) for c, o in zip(my_data.Close, my_data.Open)]
    my_data["Middle"] = (my_data.Open + my_data.Close) / 2
    my_data["Height"] = abs(my_data.Close - my_data.Open)

    my_figure = figure(x_axis_type='datetime', width=1000, height=500, responsive=True,
                       title="Price chart for {} [{} to {}]".format(symbol_name, start_moment, end_moment.date()))
    my_figure.grid.grid_line_alpha = 0.3

    hours_12 = 18 * 60 * 60 * 1000

    my_figure.segment(my_data.index, my_data.High, my_data.index, my_data.Low, color="Black")

    my_figure.rect(my_data.index[my_data.Status == "Increase"], my_data.Middle[my_data.Status == "Increase"],
                   hours_12, my_data.Height[my_data.Status == "Increase"], fill_color="#CCFFFF", line_color="black")

    my_figure.rect(my_data.index[my_data.Status == "Decrease"], my_data.Middle[my_data.Status == "Decrease"],
                   hours_12, my_data.Height[my_data.Status == "Decrease"], fill_color="#FF3333", line_color="black")

    script1, div1 = components(my_figure)
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    return render_template("plot.html",
                           script1=script1,
                           div1=div1,
                           cdn_css=cdn_css,
                           cdn_js=cdn_js)


@app.route('/')
def return_root():
    return "<html><body><span style='font-family: Verdana'>try going to <br>/SYMBOL or <br>/SYMBOL/03242017</span></body></html>"


# @app.route('/about/')
# def about():
#     return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=False, port=5555)

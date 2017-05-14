from flask import Flask, render_template
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

app = Flask(__name__)


@app.route('/<symbol_name>')
def plot(symbol_name):
    start = datetime.datetime(2016, 11, 1)
    end = datetime.datetime(2017, 3, 10)

    if not symbol_name:
        symbol_name = "GOOG"
    my_data = data.DataReader(name=symbol_name, data_source="google", start=start, end=end)

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
                       title="Price chart for {} [{} to {}]".format(symbol_name, start.date(), end.date()))
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
    return "try going to /SYMBOL"


# @app.route('/about/')
# def about():
#     return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=False)

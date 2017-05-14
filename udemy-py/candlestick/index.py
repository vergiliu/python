import datetime
from pandas_datareader import data
from bokeh.plotting import figure, show, output_file

if __name__ == "__main__":
    start_date = datetime.datetime(2017, 3, 1)
    end_date = datetime.datetime(2017, 4, 10)
    stock = "AAPL"
    dr = data.DataReader(name=stock, data_source="yahoo", start=start_date, end=end_date)
    print(dr)

    my_graph = figure(x_axis_type='datetime', width=800, height=600, title=stock)  #, y_range=(130, 150))

    twelve_hours = 12 * 60 * 60 * 1000
    red = dr.Open > dr.Close
    green = dr.Close > dr.Open

    my_graph.segment(dr.index, dr.High, dr.index, dr.Low, color="blue")
    my_graph.rect(dr.index[green], (dr.Open + dr.Close) / 2,
                  twelve_hours, abs(dr.Open - dr.Close), color="green")
    my_graph.rect(dr.index[red], (dr.Open + dr.Close) / 2,
                  twelve_hours, abs(dr.Open - dr.Close), color="red")
    output_file("data_stocks.html")
    show(my_graph)
    # online_data.index

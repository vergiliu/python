import datetime
from pandas_datareader import data
from bokeh.plotting import figure, show, output_file

if __name__ == "__main__":
    start_date = datetime.datetime(2017, 3, 1)
    end_date = datetime.datetime(2017, 3, 10)
    stock = "AAPL"
    data = data.DataReader(name=stock, data_source="google", start=start_date, end=end_date)
    print(data)

    output_graph = figure(x_axis_type='datetime', width=800, height=600, title=stock)  #, y_range=(130, 150))
    twelve_hours = 12 * 60 * 60 * 1000
    output_graph.segment(data.index, data.High, data.index, data.Low, color="blue")
    output_graph.rect(data.index[data.Close > data.Open], (data.Open + data.Close) / 2,
                      twelve_hours, abs(data.Open - data.Close), color="green")
    output_graph.rect(data.index[data.Close < data.Open], (data.Open + data.Close) / 2,
                      twelve_hours, abs(data.Open - data.Close), color="red")
    output_file("data_stocks.html")
    show(output_graph)
    # online_data.index

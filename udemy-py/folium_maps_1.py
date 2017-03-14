import folium
import pandas
# create Map object
m = folium.Map(location=[45.372, -121.696], zoom_start=8, tiles='Stamen Toner')

my_data = pandas.read_csv("Volcanoes-USA.txt")
for lat, lon, v_name in zip(my_data['LAT'], my_data['LON'], my_data['NAME']):
    folium.Marker(location=[lat, lon], popup=v_name).add_to(m)

m.save(outfile="test.html")

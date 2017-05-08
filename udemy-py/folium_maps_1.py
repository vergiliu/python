import folium
import pandas
import random
# create Map object
m = folium.Map(location=[45.372, -121.696], zoom_start=8, tiles='Stamen Terrain')
# tiles = 'Stamen Toner'

my_data = pandas.read_csv("Volcanoes-USA.txt")
random_color = ['red', 'green', 'blue', 'black']
for lat, lon, v_name in zip(my_data['LAT'], my_data['LON'], my_data['NAME']):
    colorful_icon = folium.Icon(icon='cloud', color=random_color[random.randrange(0, len(random_color)-1)])
    folium.Marker(location=[lat, lon], popup=v_name, icon=colorful_icon).add_to(m)

m.save(outfile="test.html")
